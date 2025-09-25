from django.contrib import admin
from . models import Order, OrderDetail, DiscountCode



class OrderDetailAdmin(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price_display' ,'is_paid', 'discount_display']
    list_filter = ['is_paid']
    inlines = [OrderDetailAdmin]

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "قیمت کل"


    def discount_display(self, obj):
        return obj.discount.code if obj.discount else "-"
    discount_display.short_description = "کد تخفیف"


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount', 'quantity' ,'active']
    list_filter = ['active']