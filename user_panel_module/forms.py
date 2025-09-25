from django import forms
from account_module.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده.')
        return email




class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="پسورد قبلی",
        widget=forms.PasswordInput(attrs={
            "class": "form-control ps-32 pe-60 py-16 fw-normal text-14 text-neutral-700 w-100 bg-neutral-20 border-neutral-30 border rounded-14 focus-visible-outline focus-border-main-600",
            "placeholder": "***********",
            "id": "oldPassword"
        })
    )
    new_password1 = forms.CharField(
        label="پسورد جدید",
        widget=forms.PasswordInput(attrs={
            "class": "form-control ps-32 pe-60 py-16 fw-normal text-14 text-neutral-700 w-100 bg-neutral-20 border-neutral-30 border rounded-14 focus-visible-outline focus-border-main-600",
            "placeholder": "***********",
            "id": "newPassword"
        })
    )
    new_password2 = forms.CharField(
        label="تایید پسورد",
        widget=forms.PasswordInput(attrs={
            "class": "form-control ps-32 pe-60 py-16 fw-normal text-14 text-neutral-700 w-100 bg-neutral-20 border-neutral-30 border rounded-14 focus-visible-outline focus-border-main-600",
            "placeholder": "***********",
            "id": "confirmPassword"
        })
    )
