# Generated by Django 4.1 on 2022-08-28 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]