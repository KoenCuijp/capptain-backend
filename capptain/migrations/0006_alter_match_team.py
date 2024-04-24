# Generated by Django 5.0.4 on 2024-04-24 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("capptain", "0005_match_joining_players_match_no_answer_players_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="capptain.team"
            ),
        ),
    ]
