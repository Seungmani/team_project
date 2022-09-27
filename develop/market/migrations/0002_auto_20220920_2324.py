# Generated by Django 3.2.14 on 2022-09-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-modify_dt',)},
        ),
        migrations.AddField(
            model_name='item',
            name='modify_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='modify date'),
        ),
    ]