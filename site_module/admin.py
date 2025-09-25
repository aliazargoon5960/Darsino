from django.contrib import admin
from . import models


@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'is_main_setting']
    list_editable = ['is_main_setting']



@admin.register(models.FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['Ftitle']


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']