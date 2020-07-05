# Generated by Django 3.0.8 on 2020-07-05 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user_visit", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="uservisit", options={"get_latest_by": "timestamp"},
        ),
        migrations.AddField(
            model_name="uservisit",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text="The time at which the database record was created (!=timestamp)",
            ),
            preserve_default=False,
        ),
    ]
