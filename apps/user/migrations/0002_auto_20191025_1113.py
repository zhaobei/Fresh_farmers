# Generated by Django 2.2.5 on 2019-10-25 03:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='address',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
