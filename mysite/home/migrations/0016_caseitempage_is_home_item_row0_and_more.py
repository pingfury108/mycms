# Generated by Django 5.1.3 on 2024-12-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_caseitempage_is_home_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseitempage',
            name='is_home_item_row0',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caseitempage',
            name='is_home_item_row1_left',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caseitempage',
            name='is_home_item_row1_right',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagegalleryimage',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]