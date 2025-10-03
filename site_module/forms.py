from django import forms
from .models import SiteSetting, FooterLinkBox, FooterLink, Banner

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'site_url': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'office_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'email2': forms.EmailInput(attrs={'class': 'form-control'}),
            'copy_right': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'about_us_text': forms.Textarea(attrs={'class': 'form-control', 'rows':4}),
        }

class FooterLinkBoxForm(forms.ModelForm):
    class Meta:
        model = FooterLinkBox
        fields = ['title']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'})}

class FooterLinkForm(forms.ModelForm):
    class Meta:
        model = FooterLink
        fields = ['Ftitle', 'url', 'footer_link_box']
        widgets = {
            'Ftitle': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'footer_link_box': forms.Select(attrs={'class': 'form-select'}),
        }

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        widgets = {
            'small_title': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
