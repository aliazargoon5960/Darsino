from django import forms
from .models import Article
from .models import Author

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'image']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کامل نویسنده'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
