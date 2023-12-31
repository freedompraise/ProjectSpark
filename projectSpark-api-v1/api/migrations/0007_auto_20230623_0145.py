# Generated by Django 3.2 on 2023-06-23 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_auto_20230622_2242"),
    ]

    operations = [
        migrations.AddField(
            model_name="idea",
            name="total_rating",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.CreateModel(
            name="IdeaRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField()),
                (
                    "idea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.idea"
                    ),
                ),
                (
                    "rater",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("idea", "rater")},
            },
        ),
    ]
