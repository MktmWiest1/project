# Generated by Django 4.0.1 on 2022-01-21 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_rename_descrption_twshows_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_comment', to='shows.twshows')),
            ],
        ),
    ]