# Generated by Django 5.0.7 on 2024-08-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("specialists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="specialist",
            name="description",
            field=models.TextField(
                blank=True, default="", verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="speciality",
            name="description",
            field=models.TextField(
                blank=True, default="", verbose_name="Описание"
            ),
        ),
    ]
