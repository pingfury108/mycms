# Generated by Django 5.1.3 on 2024-12-20 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_hometitle_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copywriterpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='industrycasespage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='meetingplanningpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BrandDesignPage',
        ),
        migrations.DeleteModel(
            name='CopywriterPage',
        ),
        migrations.DeleteModel(
            name='IndustryCasesPage',
        ),
        migrations.DeleteModel(
            name='MeetingPlanningPage',
        ),
    ]
