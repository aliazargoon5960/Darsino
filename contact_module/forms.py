from django import forms
from . models import Message



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'common-input rounded-pill border-transparent focus-border-main-600',
                'id': 'name',
                'placeholder': 'نام خود را وارد کنید...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'common-input rounded-pill border-transparent focus-border-main-600',
                'id': 'email',
                'placeholder': 'ایمیل را وارد کنید...'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'common-input rounded-pill border-transparent focus-border-main-600',
                'id': 'phone',
                'placeholder': 'شماره تماس وارد کنید'
            }),
            'msg': forms.Textarea(attrs={
                'class': 'common-input rounded-24 border-transparent focus-border-main-600 h-110',
                'id': 'desc',
                'placeholder': 'پیام خود را بنویسید',
                'rows': 5
            }),           

        }

    