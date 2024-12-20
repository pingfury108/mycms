# Generated by Django 5.1.3 on 2024-12-09 03:23

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_describe_pagegalleryimage_industry'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseItemPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('industry', models.CharField(blank=True, max_length=250)),
                ('describe', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': '作品案例详情',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='pagegalleryimage',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='workscasespage',
            name='body',
        ),
        migrations.AlterField(
            model_name='pagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='home.caseitempage'),
        ),
        migrations.CreateModel(
            name='NewsItemPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': '新闻动态详情',
            },
            bases=('wagtailcore.page',),
        ),
    ]
