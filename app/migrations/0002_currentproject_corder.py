# Generated by Django 3.2.9 on 2021-11-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentproject',
            name='cOrder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
