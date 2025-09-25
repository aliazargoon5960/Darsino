from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from . models import User
from django.contrib.auth import authenticate,get_user_model


class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید...'})
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی خود را وارد کنید...'})
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید...'})
    )
    password = forms.CharField(
        label='گذرواژه',
        widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه را وارد کنید...'}),
        validators=[validators.MinLengthValidator(8)]
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلا ثبت نام کرده است...")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


User = get_user_model()
class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=60, required=True, label='ایمیل',
        widget=forms.TextInput(attrs={'placeholder': 'ایمیل خود را وارد کنید...'})
    )
    password = forms.CharField(
        label='گذرواژه',
        widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه را وارد کنید...'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is None:
                raise forms.ValidationError("ایمیل یا گذرواژه اشتباه است.")
            cleaned_data['user'] = user

        return cleaned_data