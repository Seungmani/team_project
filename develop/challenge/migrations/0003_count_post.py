# Generated by Django 3.2.14 on 2022-08-23 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_profile_user_count'),
        ('challenge', '0002_delete_count_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count_Post',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.profile')),
                ('user_count', models.CharField(default='', max_length=10)),
            ],
            bases=('users.profile',),
        ),
    ]