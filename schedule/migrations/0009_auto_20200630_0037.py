# Generated by Django 3.0.7 on 2020-06-30 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20200630_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.CharField(max_length=9),
        ),
    ]
