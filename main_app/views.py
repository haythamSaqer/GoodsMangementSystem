from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, Count, Case, When, IntegerField, Sum, CharField, Value
from django import forms
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import OrderForm, ShippingCompanyForm
from .models import Order, Picture, ShippingCompany, CustomUser


class AdminRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('goods_management:order_list')
#     # redirect_authenticated_user = True


# class CustomLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#
#         # call the parent class dispatch method to handle the logout logic
#         response = super().dispatch(request, *args, **kwargs)
#
#         return response


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = 'orders'
    ordering = ['-date_created']
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        else:
            return Order.objects.filter(created_by=self.request.user)


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'main_app/order_detail.html'
    context_object_name = 'order'

    def test_func(self):
        return self.request.user.is_superuser or self.object.created_by == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Picture.objects.filter(order=self.object).order_by('-uploaded_at')
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    # form_class = OrderForm
    template_name = 'newRequest.html'
    success_url = reverse_lazy('goods_management:order_list')
    fields = ['customs_declaration_number', 'shipping_company', 'importer_name', 'note']

    def form_valid(self, form):
        print(form)
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shipping_company'] = ShippingCompany.objects.all()
        return context

    # def get_form_class(self):
    #     class DynamicForm(forms.ModelChoiceField):
    #         class Meta:
    #             model = Order
    #             fields = ['customs_declaration_number', 'shipping_company', 'importer_name']
    #
    #         shipping_company = forms.ModelChoiceField(
    #             queryset=ShippingCompany.objects.all()
    #         )
    #
    #     return DynamicForm


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'main_app/order_update.html'
    success_url = reverse_lazy('goods_management:order_list')

    def test_func(self):
        return self.request.user.is_superuser or self.object.created_by == self.request.user


# class ShippingCompanyListView(ListView):
#     model = CustomUser
#     template_name = 'main_app/employee_list.html'
#     context_object_name = 'companies'
#
#     def get_queryset(self):
#         return CustomUser.objects.filter(user_type=CustomUser.EMPLOYEE)


class ShippingCompanyCreateView(AdminRequiredMixin, CreateView):
    model = ShippingCompany
    form_class = ShippingCompanyForm
    template_name = 'main_app/create_shipping_company.html'
    success_url = reverse_lazy('goods_management:order_list')


class ShippingCompanyUpdateView(AdminRequiredMixin, UpdateView):
    model = ShippingCompany
    form_class = ShippingCompanyForm
    template_name = 'main_app/update_shipping_company.html'
    success_url = reverse_lazy('goods_management:order_list')


class EmployeeListView(ListView):
    model = CustomUser
    template_name = 'employee.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=CustomUser.EMPLOYEE)


class EmployeeCreateView(AdminRequiredMixin, CreateView):
    model = CustomUser
    template_name = 'main_app/employee_create.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'password', 'user_type']
    success_url = reverse_lazy('goods_management:employee-list')

    def form_valid(self, form):
        form.instance.is_employee = True
        return super().form_valid(form)


class EmployeeUpdateView(AdminRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'update_employee.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'password', 'user_type', 'name']
    success_url = reverse_lazy('goods_management:employee-list')

    def form_valid(self, form):
        form.instance.is_employee = True
        return super().form_valid(form)


class KPAReportView(ListView):
    model = ShippingCompany
    template_name = 'main_app/kpa_report.html'

    # context_object_name = 'shipping_companies'

    def get_queryset(self):
        # get query parameters
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        # if no query parameters are specified, default to a month
        if not start_date and not end_date:
            end_date = timezone.now()
            start_date = end_date - timezone.timedelta(days=30)

        orders = Order.objects.filter(created_at__range=(start_date, end_date))
        late_deliveries = Q(accepted_at__lt=timezone.make_aware(
            timezone.datetime.combine(orders.first().created_at.date(), timezone.datetime.min.time()))) | Q(
            accepted_at__isnull=True)
        on_time_deliveries = Q(accepted_at__lt=timezone.make_aware(
            timezone.datetime.combine(orders.first().created_at.date(), timezone.datetime.max.time()))) & Q(
            accepted_at__gt=timezone.make_aware(
                timezone.datetime.combine(orders.first().created_at.date(), timezone.datetime.min.time())))

        orders = orders.annotate(
            delivery_status_s=Case(
                When(late_deliveries, then=Value('late_delivery')),
                When(on_time_deliveries, then=Value('on_time_delivery')),
                default=Value('early_delivery'),
                output_field=CharField()
            )
        )
        orders = orders.filter(delivery_status_s__exact='late_delivery')
        print(orders)

        # aggregate orders by delivery company and delivery status
        companies = ShippingCompany.objects.annotate(
            num_orders=Count('order'),
            late_deliveries=Sum(
                Case(
                    When(Q(order__delivery_status='late_delivery'), then=1),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            on_time_deliveries=Sum(
                Case(
                    When(Q(order__delivery_status='on_time_delivery'), then=1),
                    default=0,
                    output_field=IntegerField()
                )
            ),
            early_deliveries=Sum(
                Case(
                    When(Q(order__delivery_status='early_delivery'), then=1),
                    default=0,
                    output_field=IntegerField()
                )
            ),
        )

        # calculate KPA for each company
        for company in companies:
            company.kpa = (((company.on_time_deliveries * 1) + (company.early_deliveries * 0.5) + (
                    company.late_deliveries * 0)) / company.num_orders) * 100 if company.num_orders else 0
            company.save()
        # print(companies.values())
        return companies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # add filters to context
        context['start_date'] = self.request.GET.get('start_date')
        context['end_date'] = self.request.GET.get('end_date')

        return context
