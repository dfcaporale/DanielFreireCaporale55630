# Generated by Django 4.2.3 on 2023-08-31 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTickets', '0004_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='webpage',
            field=models.URLField(max_length=50),
        ),
    ]
