# Generated by Django 2.1.5 on 2019-08-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20190801_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
