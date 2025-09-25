from django.db import models
from django.urls import reverse
from slugify import slugify  

class Author(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='نام کامل')
    image = image = models.ImageField(upload_to="image/author", verbose_name='عکس')

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'

    def __str__(self):
        return self.fullname
    

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='article', verbose_name='نویسنده')
    image = models.ImageField(upload_to="image/article", verbose_name='عکس')
    description = models.TextField(verbose_name='متن مقاله')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='اسلاگ')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse("blog_module:article_detail", args=[self.slug])
        
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title
