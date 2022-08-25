# Generated by Django 4.1 on 2022-08-25 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('story', models.TextField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=150)),
                ('neighborhood', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['shop_name'],
            },
        ),
    ]
