# Generated by Django 4.1 on 2024-02-23 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_jam_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tune',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]