# Generated by Django 1.10.2 on 2016-10-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_appownershiptransfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='ocsid',
            field=models.IntegerField(blank=True, help_text='Old store id. Deprecated', null=True, unique=True, verbose_name='OCS id'),
        ),
    ]
