# Generated by Django 2.1.5 on 2019-08-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0007_auto_20190801_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.CharField(choices=[('RP', 'Roshan Pandey'), ('BH', 'Bharat Hasija')], default='RP', max_length=2),
        ),
    ]
