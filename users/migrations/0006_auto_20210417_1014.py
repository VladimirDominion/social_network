# Generated by Django 3.1.7 on 2021-04-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_useractivity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='api_url',
            field=models.TextField(blank=True, default=''),
        ),
    ]
