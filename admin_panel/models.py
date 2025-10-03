from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify


User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            counter = 1
            while Course.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title




class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='articles/thumbnails/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            counter = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)
    answered_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='answered_contacts')
    answered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} — {self.subject or 'بدون موضوع'}"




class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'باز'),
        ('pending', 'در انتظار'),
        ('closed', 'بسته'),
    )
    PRIORITY = (
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=10, choices=PRIORITY, default='medium')
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tickets')
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"#{self.pk} {self.subject}"




class SliderImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='site/slider/')
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['order']


    def __str__(self):
        return self.title or f"اسلایدر {self.pk}"




class SiteSetting(models.Model):
    site_name = models.CharField(max_length=255, default='درسینو')
    logo = models.ImageField(upload_to='site/logo/', null=True, blank=True)
    footer_text = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return 'تنظیمات سایت'

