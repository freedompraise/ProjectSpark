# Generated by Django 3.2 on 2023-06-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20230623_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]