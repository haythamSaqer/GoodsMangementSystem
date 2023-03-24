from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

# , OrderUpdateView, OrderDeleteView

app_name = 'goods_management'

urlpatterns = [

    # path('login/', CustomLoginView.as_view(), name='login'),  # new

    path('', OrderListView.as_view(), name='order_list'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    # path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    # path('company/list/', ShippingCompanyListView.as_view(), name='company-list'),
    path('shipping-companies/create/', ShippingCompanyCreateView.as_view(), name='shippingcompany-create'),
    path('shipping-companies/<int:pk>/update/', ShippingCompanyUpdateView.as_view(), name='shippingcompany-update'),
    path('employee/list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),

    path('kpa-report', KPAReportView.as_view(), name='kpa_report'),

    # path("chat/", index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
