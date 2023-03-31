# Generated by Django 3.0.3 on 2021-08-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Available'), (2, 'Do Not Disturb'), (3, 'Asleep')], default=1),
        ),
    ]