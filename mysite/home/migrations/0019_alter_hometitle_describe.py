# Generated by Django 5.1.3 on 2024-12-13 05:42

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_hometitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometitle',
            name='describe',
            field=wagtail.fields.StreamField([('p', 0)], block_lookup={0: ('wagtail.blocks.CharBlock', (), {'blank': True})}),
        ),
    ]