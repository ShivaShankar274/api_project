# Generated by Django 5.2.4 on 2025-07-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimodel',
            name='unum',
            field=models.BigIntegerField(),
        ),
    ]
