# Generated by Django 3.0.4 on 2020-05-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_ordered',
        ),
    ]
