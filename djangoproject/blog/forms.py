from .models import Post
from django.forms import ModelForm, DateTimeInput, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'short_description', 'text', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Кратко о чём статья'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Полный текст статьи'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'})
        }
