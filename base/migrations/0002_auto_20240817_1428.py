# Generated by Django 3.2.13 on 2024-08-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='good_count',
            field=models.PositiveIntegerField(default=0, verbose_name='いいね'),
        ),
        migrations.AddField(
            model_name='item',
            name='read_count',
            field=models.PositiveIntegerField(default=0, verbose_name='閲覧数'),
        ),
        migrations.AddField(
            model_name='item',
            name='usertext',
            field=models.CharField(default='a', max_length=50, verbose_name='user_itemの紐付け用'),
        ),
    ]
