from django.db import models

from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Vendor(models.Model):

    vendor_name = models.CharField(max_length=20)  # 店家的名稱
    vendor_phone = models.CharField(max_length=10)  # 攤販的電話

    def __str__(self):
        return self.vendor_name

    def get_absolute_url(self):
        return reverse("vendors:vendor_id", kwargs={"id": self.id})


class Food(models.Model):

    food_name = models.CharField(max_length=30)  # 食物的名稱
    price_name = models.DecimalField(max_digits=3, decimal_places=0)  # 食物價錢
    food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)  # 代表這食物是由哪一個攤販所做的

    def __str__(self):
        return self.food_name


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_name', 'vendor_phone')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_name', 'price_name', 'food_vendor')
    list_filter = ('price_name',)
    search_fields = ('food_name', 'price_name')  # 搜尋欄位
