# Generated by Django 4.0.1 on 2022-01-13 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_posts_delete_post1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Book',
        ),
    ]
