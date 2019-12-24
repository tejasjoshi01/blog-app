from django.forms import ModelForm
from .models import Blog

class WriteBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']


