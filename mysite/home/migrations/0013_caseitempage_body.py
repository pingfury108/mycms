# Generated by Django 5.1.3 on 2024-12-11 03:36

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_aboutpage_team_image_loggalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseitempage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
