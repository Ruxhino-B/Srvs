# Generated by Django 3.2.4 on 2021-08-11 08:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sherbim', '0011_alter_shto_sherbim_sherbimi_rradhes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shto_sherbim',
            name='sherbimi_rradhes',
            field=models.DateField(default=datetime.datetime(2021, 11, 19, 8, 7, 27, 116404, tzinfo=utc)),
        ),
    ]
