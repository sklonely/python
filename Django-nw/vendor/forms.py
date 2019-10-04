from django import forms  # 從django 本體 導入forms

from .models import Vendor, Food  # 從.models 導入自製的 Vendor and Food

from django.utils.translation import gettext_lazy as _  # 網頁 labels 用


class RawVendorForm(forms.Form):

    vendor_name = forms.CharField(label='商家名稱')
    phone_number = forms.CharField(label='商家電話')


class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor  # 對應 vendor 資料
        fields = '__all__'  # 取得全部欄位

        labels = {
            'vendor_name': _('商家名稱'),
            'vendor_phone': _('商家電話'),
        }