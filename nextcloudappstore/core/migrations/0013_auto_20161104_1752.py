# Generated by Django 1.10.2 on 2016-11-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20161015_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='rating_num_overall',
            field=models.IntegerField(default=0, verbose_name='Number of overall casted rating'),
        ),
        migrations.AddField(
            model_name='app',
            name='rating_num_recent',
            field=models.IntegerField(default=0, verbose_name='Number of recently casted ratings'),
        ),
    ]
