# Generated by Django 2.2.4 on 2020-12-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageupload',
            name='name',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
