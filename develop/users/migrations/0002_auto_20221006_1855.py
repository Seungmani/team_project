# Generated by Django 3.2.14 on 2022-10-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_background',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/', verbose_name='배경사진'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/', verbose_name='프로필사진'),
        ),
    ]