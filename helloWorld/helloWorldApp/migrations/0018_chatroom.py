# Generated by Django 2.2.5 on 2019-12-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorldApp', '0017_suggestion_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]