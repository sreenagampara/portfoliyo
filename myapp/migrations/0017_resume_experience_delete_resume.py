# Generated by Django 4.0.1 on 2022-05-03 15:25

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_project_bg_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, default='Null', max_length=2000)),
                ('company', models.CharField(blank=True, default='Null', max_length=2000)),
                ('details', models.TextField(blank=True, default='Null')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='resume',
        ),
    ]