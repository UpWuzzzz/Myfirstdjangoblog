# Generated by Django 2.0.4 on 2018-05-14 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Img',
        ),
    ]
