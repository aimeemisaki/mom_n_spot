from xmlrpc.client import DateTime
from django.db import models
import time
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    shop_name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    story = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    neighborhood = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name, self.img, self.story, self.neighborhood, self.address, self.user

    class Meta:
        ordering = ['shop_name']