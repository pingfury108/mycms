# Generated by Django 5.1.3 on 2024-12-09 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_pagegalleryimage_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='body',
        ),
    ]
