from django.db import models
from django.urls import reverse
from slugify import slugify  
from account_module.models import User

class Teacher(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="اسم کامل")
    image = models.ImageField(upload_to='image/Teacher', verbose_name='عکس استاد')
    job = models.CharField(max_length=200, verbose_name='تخصص استاد')
    bio = models.TextField(verbose_name='بیوگرافی')
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='ایمیل')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "استاد ها"

    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Teacher, self).save()

    def get_absolute_url(self):
        return reverse("course_module:teacher_detail", args=[self.slug])

    def __str__(self):
        return f"{self.fullname} - {self.email}"
    


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
    

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'مبتدی'),
        ('intermediate', 'متوسط'),
        ('advanced', 'حرفه‌ای'),
    ]

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='استاد دوره', related_name="course")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی دوره", related_name="course")
    title = models.CharField(max_length=100, verbose_name='عنوان دوره')
    description = models.TextField(verbose_name='توضیحات دوره')
    price = models.IntegerField(default=0, db_index=True, verbose_name='قیمت')
    image = models.ImageField(upload_to="image/course", verbose_name='عکس')
    duration = models.CharField(max_length=100, verbose_name='طول دوره')
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    created = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="اسلاگ")
    status = models.BooleanField(verbose_name='وضعیت دوره')
    fav_students = models.ManyToManyField(User, related_name="fav_courses", blank=True)

    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save()

    def get_absolute_url(self):
        return reverse("course_module:course_detail", args=[self.slug])
    
    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="comments", verbose_name='دوره')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True ,blank=True ,related_name='replies', verbose_name='پاسخ به نظر')
    body = models.TextField(verbose_name='نظر کاربر')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
    
    def __str__(self):
        return  f"{self.course.title} - {self.body[:20]}"
