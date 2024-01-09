# Generated by Django 5.0.1 on 2024-01-09 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aut_com", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="parent_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="aut_com.comment",
            ),
        ),
    ]
