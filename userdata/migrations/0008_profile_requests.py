# Generated by Django 3.0.3 on 2021-08-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0007_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='requests',
            field=models.ManyToManyField(to='userdata.Profile'),
        ),
    ]
