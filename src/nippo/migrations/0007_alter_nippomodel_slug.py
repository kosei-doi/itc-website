# Generated by Django 4.1.3 on 2023-01-15 01:10

from django.db import migrations, models
import nippo.models


class Migration(migrations.Migration):

    dependencies = [
        ('nippo', '0006_nippomodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nippomodel',
            name='slug',
            field=models.SlugField(default=nippo.models.slug_maker, max_length=20, unique=True),
        ),
    ]
