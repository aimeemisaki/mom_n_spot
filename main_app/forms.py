from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('shop_name', 'img', 'story', 'category', 'neighborhood', 'user')
        