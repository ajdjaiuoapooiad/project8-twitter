# Generated by Django 3.2.13 on 2024-08-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bg_image',
            field=models.ImageField(blank=True, default='static/sample_image/pexels-eberhardgross-443446 (1).jpg', upload_to='static/image/', verbose_name='背景画像'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/sample_image/kkrn_icon_user_1.png', upload_to='static/image/', verbose_name='アイコン画像'),
        ),
    ]