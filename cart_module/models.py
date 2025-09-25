from django.db import models
from account_module.models import User
from course_module.models import Course
from django.db.models import Sum, F



class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="کد تخفیف")
    amount = models.IntegerField(verbose_name="مقدار تخفیف (تومان)")
    active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    quantity = models.IntegerField(default=1,verbose_name="تعداد کد تخفیف")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name="نهایی شده/نشده", default=False)
    payment_date = models.DateField(verbose_name='تاریخ پرداخت', null=True, blank=True)
    discount = models.ForeignKey(DiscountCode, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کد تخفیف")
    

    def __str__(self):
        return str(self.user)
    
    @property
    def total_price(self):
        total = self.items.aggregate(total=Sum(F('price')))['total'] or 0
        if self.discount and self.discount.active:
            total -= self.discount.amount
            if total < 0:
                total = 0
        return total



    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = " سبد خرید کاربران " 

    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سبد خرید')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='items', verbose_name='دوره')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تک محصول')

    def __str__(self):
        return str(self.order)
    
    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'جزییات سبد خرید'


