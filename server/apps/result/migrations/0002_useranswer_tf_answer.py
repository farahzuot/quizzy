# Generated by Django 4.2.10 on 2024-03-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useranswer",
            name="tf_answer",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]