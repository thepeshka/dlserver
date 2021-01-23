# Generated by Django 3.0.9 on 2021-01-23 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20200803_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='is_latest',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('target_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.File')),
                ('target_version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.Version')),
            ],
        ),
    ]