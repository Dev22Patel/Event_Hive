# Generated by Django 5.0.2 on 2024-02-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventapp', '0006_remove_event_sponsortypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='EventName',
            field=models.CharField(default='Not specified', max_length=255),
        ),
    ]