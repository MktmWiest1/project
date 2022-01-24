# Generated by Django 4.0.1 on 2022-01-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_expert_expertrecomendation_delete_bookexperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertrecomendation',
            name='selection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='book.book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expert',
            name='info_exp',
            field=models.TextField(max_length=100),
        ),
    ]