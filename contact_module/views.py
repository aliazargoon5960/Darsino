from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, FormView
from . models import Message
from . forms import MessageForm
from site_module.models import SiteSetting


class ContactUsView(View):
    def get(self, request):
        form = MessageForm()
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        return render(request, "contact_module/contact_us.html", {'form' : form, 'setting':site_setting})
    
    def post(self, request):
        form = MessageForm(request.POST)
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        if form.is_valid():
            form.save()
            form = MessageForm()
        return render(request, "contact_module/contact_us.html", {'form' : form, 'setting':site_setting})
   