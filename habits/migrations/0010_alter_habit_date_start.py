# Generated by Django 5.1 on 2024-08-30 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0009_alter_habit_date_start"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="date_start",
            field=models.DateField(
                default=datetime.datetime.now, verbose_name="Дата начала"
            ),
        ),
    ]
