# Generated by Django 4.0.3 on 2022-04-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RezhApp', '0002_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleimage',
            name='caption',
            field=models.CharField(max_length=255, null=True),
        ),
    ]