# Generated by Django 4.0.1 on 2022-04-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='author_resume',
        ),
        migrations.AddField(
            model_name='resume',
            name='author_resume1',
            field=models.CharField(blank=True, default='Null', max_length=2000),
        ),
        migrations.AddField(
            model_name='resume',
            name='author_resume2',
            field=models.CharField(blank=True, default='Null', max_length=2000),
        ),
        migrations.AddField(
            model_name='resume',
            name='author_resume3',
            field=models.CharField(blank=True, default='Null', max_length=2000),
        ),
        migrations.AlterField(
            model_name='resume',
            name='bg_image',
            field=models.CharField(blank=True, default='Null', max_length=2000),
        ),
    ]
