# Generated by Django 4.0.3 on 2022-03-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]