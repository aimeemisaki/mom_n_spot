from xmlrpc.client import DateTime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
# Category Choices
category_choices = [
    ('Deli', 'deli'),
    ('Restaurant', 'restaurant'),
    ('Apparel', 'apparel'),
    ('Art Supplies', 'art supplies'),
    ('Beauty Supplies', 'beauty supplies'),
    ('Bookshop','bookshop'),
    ('Drug Store', 'drug store'),
    ('Grocery Store', 'grocery store'),
    ('Plant Nursery','plant nursery'),
    ('Children Boutique', 'children boutiques'),
    ('Other', 'other'),
]

neighborhood_choices = [
    ('East and Northeast LA', 'east northeast'),
    ('Downtown LA', 'downtown'),
    ('Echo Park and Westlake', 'echopark westlake'),
    ('Hollywood', 'hollywood'),
    ('Harbor Area', 'harbor area'),
    ('Los Feliz and Silverlake', 'los feliz silverlake'),
    ( 'South Central', 'south central'),
    ('San Fernando Valley', 'sfv'),
    ('West LA', 'west'),
    ('Wilshire', 'wilshire'),
]

class Post(models.Model):
    shop_name = models.CharField(max_length=200)
    img = models.FileField(
        validators=[FileExtensionValidator(['pdf', 'png', 'jpg', 'jpeg', 'webp', 'svg', 'heic'])])
    story = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=150, choices=category_choices)
    neighborhood = models.CharField(max_length=150, choices=neighborhood_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    class Meta:
        ordering = ['shop_name']

class Tag(models.Model):
    title = models.CharField(max_length=150)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title