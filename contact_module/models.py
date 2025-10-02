from django.db import models





class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=12, verbose_name='شماره تلفن')
    msg = models.TextField(verbose_name='پیغام کاربر')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return f'{self.name}-{self.msg[:30]}'
