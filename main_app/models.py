from django.db import models
import time
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    restaurant_name = models.CharField(max_lenght=200)