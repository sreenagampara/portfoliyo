# Generated by Django 4.0.1 on 2022-04-26 03:26

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_contact'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
