# Generated by Django 5.1.7 on 2025-03-15 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_remove_blog_summary_blog_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="title",
        ),
    ]
