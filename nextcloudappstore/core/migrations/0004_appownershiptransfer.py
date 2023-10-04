# Generated by Django 1.10.1 on 2016-09-26 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_appreleasedeletelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppOwnershipTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposed', models.DateTimeField(auto_now_add=True)),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ownership_transfer', to='core.App')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_ownership_transfers_outgoing', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_ownership_transfers_incoming', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
