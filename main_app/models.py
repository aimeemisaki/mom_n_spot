from xmlrpc.client import DateTime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
# Category Choices
category_choices = [
    ('deli', 'Deli'),
    ('restaurant', 'Restaurant'),
    ('apparel', 'Apparel'),
    ('art supplies', 'Art Supplies'),
    ('bookshop', 'Bookshops'),
    ('drug store', 'Drug Store'),
    ('grocery store', 'Grocery Store'),
    ('plant nursery', 'Plant Nursery'),
    ('other', 'Other')
]

neighborhood_choices = [
    ('east northeast', 'East and Northeast LA'),
    ('downtown', 'Downtown LA'),
    ('echopark westlake', 'Echo Park and Westlake'),
    ('hollywood', 'Hollywood'),
    ('harbor area', 'Harbor Area'),
    ('los feliz silverlake', 'Los Feliz and Silverlake'),
    ('south central', 'South Central'),
    ('sfv', 'San Fernando Valley'),
    ('west', 'West LA'),
    ('wilshire', 'Wilshire'),

]

class Post(models.Model):
    shop_name = models.CharField(max_length=200)
    img = models.FileField(upload_to="posts/imgs/",
        validators=[FileExtensionValidator(['pdf', 'png', 'jpg', 'svg', 'heic'])])
    story = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=150, choices=category_choices)
    neighborhood = models.CharField(max_length=150, choices=neighborhood_choices)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    class Meta:
        ordering = ['shop_name']

class Tags(models.Model):
    title = models.CharField(max_length=150)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title, self.posts