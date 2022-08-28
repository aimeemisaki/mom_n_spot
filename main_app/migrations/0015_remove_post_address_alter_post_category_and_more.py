# Generated by Django 4.1 on 2022-08-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='address',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Deli', 'deli'), ('Restaurant', 'restaurant'), ('Apparel', 'apparel'), ('Art Supplies', 'art supplies'), ('Beauty Supplies', 'beauty supplies'), ('Bookshop', 'bookshop'), ('Drug Store', 'drug store'), ('Grocery Store', 'grocery store'), ('Plant Nursery', 'plant nursery'), ('Children Boutique', 'children boutiques'), ('Other', 'other')], max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='neighborhood',
            field=models.CharField(choices=[('East and Northeast LA', 'east northeast'), ('Downtown LA', 'downtown'), ('Echo Park and Westlake', 'echopark westlake'), ('Hollywood', 'hollywood'), ('Harbor Area', 'harbor area'), ('Los Feliz and Silverlake', 'los feliz silverlake'), ('South Central', 'south central'), ('San Fernando Valley', 'sfv'), ('West LA', 'west'), ('Wilshire', 'wilshire')], max_length=150),
        ),
    ]
