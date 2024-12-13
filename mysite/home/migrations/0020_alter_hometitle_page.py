# Generated by Django 5.1.3 on 2024-12-13 05:46

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_hometitle_describe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometitle',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='heads', to='home.homepage'),
        ),
    ]
