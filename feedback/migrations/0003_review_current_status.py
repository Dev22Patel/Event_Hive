# Generated by Django 5.0.3 on 2024-03-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='current_status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
