# Generated by Django 4.1 on 2022-08-26 02:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg', 'svg'])]),
        ),
    ]
