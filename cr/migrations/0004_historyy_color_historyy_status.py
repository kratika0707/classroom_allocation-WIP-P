# Generated by Django 4.1.7 on 2023-11-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyy',
            name='color',
            field=models.CharField(default='red', max_length=50),
        ),
        migrations.AddField(
            model_name='historyy',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
