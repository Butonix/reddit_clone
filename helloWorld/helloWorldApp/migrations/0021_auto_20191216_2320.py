# Generated by Django 2.2.5 on 2019-12-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorldApp', '0020_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, max_length=144, null=True, upload_to='static/images/'),
        ),
    ]
