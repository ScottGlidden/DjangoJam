# Generated by Django 5.0.2 on 2024-03-01 11:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("django_jam_app", "0004_tune_beats_per_minute_alter_tune_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tune",
            old_name="artist",
            new_name="creator",
        ),
    ]
