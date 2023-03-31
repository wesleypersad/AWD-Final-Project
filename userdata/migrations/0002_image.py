# Generated by Django 3.0.3 on 2021-07-29 18:09

from django.db import migrations, models
import django.db.models.deletion
import userdata.models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=userdata.models.upload_gallery_image)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='userdata.Profile')),
            ],
        ),
    ]
