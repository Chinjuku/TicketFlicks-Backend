# Generated by Django 5.0.4 on 2024-05-07 05:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_actor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fbda4824-9bc3-4320-bc83-b074613ae52b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
