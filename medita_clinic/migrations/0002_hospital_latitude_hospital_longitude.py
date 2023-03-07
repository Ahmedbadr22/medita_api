# Generated by Django 4.1.3 on 2023-02-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medita_clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='hospital',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]