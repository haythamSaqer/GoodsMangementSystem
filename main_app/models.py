from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'
    DELIVERY_COMPANY = 'delivery_company'

    USER_TYPES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('delivery', 'Delivery'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=25, null=True)
    name = models.CharField(max_length=50, null=True)

    def is_admin(self):
        return self.user_type == self.ADMIN

    def is_employee(self):
        return self.user_type == self.EMPLOYEE

    def is_delivery_company(self):
        return self.user_type == self.DELIVERY_COMPANY


class ShippingCompany(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='shipping_company', null=True,
                                unique=True)
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    status = (
        ('accept', 'Accept'),
        ('refund', 'Refund'),
    )

    DELIVERY_STATUS_CHOICES = [
        ('early_delivery', 'early_delivery'),
        ('on_time_delivery', 'on_time_delivery'),
        ('late_delivery', 'late_delivery'),
    ]

    customs_declaration_number = models.CharField(max_length=50)
    shipping_company = models.ForeignKey(ShippingCompany, on_delete=models.CASCADE)
    importer_name = models.CharField(max_length=50, null=True)
    order_status = models.CharField(max_length=10, choices=status, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_orders')
    accepted_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='accepted_orders')
    accepted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    submitted_date = models.DateTimeField(null=True, blank=True)
    note = models.TextField(null=True)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='early_delivery')

    @property
    def kpa(self):
        """
        Calculate KPA rate for the order based on delivery date.
        """
        created_at = self.created_at.date()
        if self.submitted_date is None:
            return 0
        elif self.submitted_date.date() == created_at:
            return 100
        elif self.submitted_date.date() == created_at + timezone.timedelta(days=1):
            return 50
        elif self.submitted_date.date() > created_at + timezone.timedelta(days=1):
            return 25
        else:
            return 0

    def __str__(self):
        return self.customs_declaration_number


class Picture(models.Model):
    image = models.ImageField(upload_to='order_pictures')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pictures')
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uploaded_pictures')
    uploaded_at = models.DateTimeField(auto_now_add=True)
