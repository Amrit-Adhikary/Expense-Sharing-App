# Generated by Django 4.2 on 2024-04-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_expensegroup_assigned_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlement',
            name='is_payement_done',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
