# Generated by Django 4.1.5 on 2023-01-23 15:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dwitter", "0002_dwitter"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Dwitter",
            new_name="Dweet",
        ),
    ]
