# Generated by Django 3.0.9 on 2020-08-03 21:37

from django.db import migrations, models
import files.models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='mime_type',
        ),
        migrations.AddField(
            model_name='version',
            name='slug',
            field=models.CharField(default=files.models.slug, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
