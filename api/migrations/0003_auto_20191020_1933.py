# Generated by Django 2.1.5 on 2019-10-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191020_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='lat',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='report',
            name='lng',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
    ]
