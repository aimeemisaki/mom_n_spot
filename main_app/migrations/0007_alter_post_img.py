# Generated by Django 4.1 on 2022-08-26 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(upload_to='document/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg', 'svg'])]),
        ),
    ]
