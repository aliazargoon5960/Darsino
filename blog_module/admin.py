from django.contrib import admin
from . models import Author , Article




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

admin.site.register(Author)

