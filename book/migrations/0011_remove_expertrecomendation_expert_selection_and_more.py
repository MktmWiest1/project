# Generated by Django 4.0.1 on 2022-01-24 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_expertrecomendation_selection_alter_expert_info_exp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertrecomendation',
            name='expert_selection',
        ),
        migrations.RemoveField(
            model_name='expertrecomendation',
            name='selection',
        ),
        migrations.DeleteModel(
            name='Expert',
        ),
        migrations.DeleteModel(
            name='ExpertRecomendation',
        ),
    ]