# Generated by Django 5.0.4 on 2024-05-08 12:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_actor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0a99324a-570e-4693-afbc-7ce7dc5567ed'), editable=False, primary_key=True, serialize=False),
        ),
    ]
