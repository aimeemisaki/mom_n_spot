from xmlrpc.client import DateTime
from django.db import models
import time
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    shop_name = models.CharField(max_length=200)
    img = models.ImageField()
    story = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name, self.img, self.story, self.neighborhood, self.address, self.user, self.created_at
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    class Meta:
        ordering = ['shop_name']

class Tags(models.Model):
    title = models.CharField(max_length=150)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title, self.posts