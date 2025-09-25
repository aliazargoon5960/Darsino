from django.db import models
from account_module.models import User
from django.core.exceptions import ValidationError


class Ticket(models.Model):
    STATUS_OPEN = 'open'
    STATUS_PENDING = 'pending'
    STATUS_ANSWERED = 'answered'
    STATUS_CLOSED = 'closed'
    STATUS_CHOICES = [
        (STATUS_OPEN, 'باز'),
        (STATUS_PENDING, 'در حال بررسی'),
        (STATUS_ANSWERED, 'پاسخ داده شده'),
        (STATUS_CLOSED, 'بسته شده'),
    ]


    PRIORITY_LOW = 'low'
    PRIORITY_NORMAL = 'normal'
    PRIORITY_HIGH = 'high'
    PRIORITY_URGENT = 'urgent'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'کم'),
        (PRIORITY_NORMAL, 'معمولی'),
        (PRIORITY_HIGH, 'زیاد'),
        (PRIORITY_URGENT, 'فوری'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets', verbose_name='کاربر')
    subject = models.CharField(max_length=255, verbose_name='عنوان')
    message = models.TextField(verbose_name=' متن تیکت ')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_OPEN, verbose_name='وضعیت')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=PRIORITY_NORMAL, verbose_name='اولویت')
    is_read_by_staff = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')
    is_read_by_user = models.BooleanField(default=True, verbose_name='خوانده شده توسط کاربر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='به روزرسانی شده در')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت‌ها'
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        name = self.user.get_full_name() or self.user.username
        return f"{self.subject} — {name}"

    def last_reply(self):
        return self.replies.order_by('-created_at').first()

    def reply_count(self):
        return self.replies.count()
    
    


class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='replies', verbose_name='تیکت')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر/ادمین')
    message = models.TextField(verbose_name='متن پاسخ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='به روزرسانی شده در')

    class Meta:
        verbose_name = 'پاسخ تیکت'
        verbose_name_plural = 'پاسخ‌ها'
        ordering = ['created_at']

    def __str__(self):
        return f"پاسخ به «{self.ticket.subject}» — {self.user.username}"
    

class TicketAttachment(models.Model):
    ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE, related_name='attachments')
    reply = models.ForeignKey(TicketReply, null=True, blank=True, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='tickets/attachments/', verbose_name='فایل')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'فایل تیکت'
        verbose_name_plural = 'فایل‌ها'

    def clean(self):
        if not (self.ticket or self.reply):
            raise ValidationError('فایل باید به تیکت یا پاسخ متصل باشد.')

    def __str__(self):
        return self.file.name

