from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .forms import OrderForm, PictureForm
from .models import Order, Picture


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == 'admin'


class EmployeeRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == 'employee'


class DeliveryRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_type == 'delivery'


@method_decorator(login_required, name='dispatch')
class OrderCreateView(EmployeeRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrderAcceptanceView(AdminRequiredMixin, UpdateView):
    model = Order
    fields = []

    def form_valid(self, form):
        form.instance.accepted_by = self.request.user
        form.instance.accepted_at = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('order-list')


class PictureAttachmentView(DeliveryRequiredMixin, CreateView):
    model = Picture
    form_class = PictureForm

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        form.instance.order = get_object_or_404(Order, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('order-detail', kwargs={'pk': self.kwargs['pk']})


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'main_app/order_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Order.objects.all()
        elif user.user_type == 'employee':
            return Order.objects.filter(created_by=user)
        elif user.user_type == 'delivery':
            return Order.objects.filter(pictures__uploaded_by=user).distinct()


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'main_app/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Order.objects.all()
        elif user.user_type == 'employee':
            return Order.objects.filter(created_by=user)
        elif user.user_type == 'delivery':
            return Order.objects.filter(pictures__uploaded_by=user).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PictureForm()
        return context
