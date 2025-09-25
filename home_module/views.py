from django.shortcuts import render
from django.views.generic import TemplateView
from course_module.models import Course, Category,Teacher
from django.shortcuts import get_object_or_404
from blog_module.models import Article
from site_module.models import Banner, SiteSetting

class HomeView(TemplateView):
    template_name = "home_module/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Banner.objects.filter(is_active=True).first()
        context['courses'] = Course.objects.all().order_by('-created')
        context['category'] = Category.objects.all()
        context['teacher'] = Teacher.objects.all()
        context['active_category'] = None  
        context['articles'] = Article.objects.all().order_by('-created_at')[:3]
        context['setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context


class AboutUsView(TemplateView):
    template_name = "home_module/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context