# Generated by Django 4.0.1 on 2022-01-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_rename_descrptions_twshows_descrption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twshows',
            old_name='descrption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='twshows',
            old_name='genger',
            new_name='genre',
        ),
        migrations.AlterField(
            model_name='twshows',
            name='data_filmed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
