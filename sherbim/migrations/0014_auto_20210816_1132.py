# Generated by Django 3.2.4 on 2021-08-16 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sherbim', '0013_alter_shto_sherbim_sherbimi_rradhes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lloj_sherbimi',
            name='cmimi',
        ),
        migrations.AlterField(
            model_name='shto_sherbim',
            name='sherbimi_rradhes',
            field=models.DateField(default=datetime.datetime(2021, 11, 24, 9, 32, 2, 317964, tzinfo=utc)),
        ),
    ]
