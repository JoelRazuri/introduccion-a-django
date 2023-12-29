from django import forms
from .models import Post

class PostCreateFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')