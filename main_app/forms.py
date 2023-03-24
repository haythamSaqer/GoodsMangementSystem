from django import forms

from .models import Order, Picture, ShippingCompany, CustomUser
from django.utils.translation import gettext as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customs_declaration_number', 'shipping_company', 'importer_name']


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True


class ShippingCompanyForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, strip=False)

    class Meta:
        model = ShippingCompany
        exclude = ('user',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        try:
            user = CustomUser.objects.get(username=self.cleaned_data.get("name"))

        except:
            user = CustomUser.objects.create_user(
                username=self.cleaned_data['name'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password1'],
                user_type='delivery',
            )
        shipping_company = super().save(commit=False)
        shipping_company.user = user
        if commit:
            shipping_company.save()
        return shipping_company