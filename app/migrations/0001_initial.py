# Generated by Django 3.2.8 on 2021-11-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projName', models.CharField(max_length=255)),
                ('projDesc', models.CharField(blank=True, max_length=255)),
                ('projSource', models.CharField(blank=True, max_length=255)),
                ('projLink', models.CharField(blank=True, max_length=255)),
                ('projOrg', models.CharField(blank=True, max_length=255)),
                ('theType', models.IntegerField(choices=[{'id': 0, 'type': 'Front End'}, {'id': 1, 'type': 'Back End'}, {'id': 2, 'type': 'Full Stack'}, {'id': 3, 'type': 'Organization'}], default=0)),
                ('theStatus', models.IntegerField(choices=[{'id': 0, 'status': 'Current'}, {'id': 1, 'status': 'Past'}], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('linkedIn', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currName', models.CharField(max_length=255)),
                ('currDesc', models.CharField(max_length=255)),
                ('currImg', models.CharField(max_length=255)),
                ('currSource', models.CharField(blank=True, max_length=255)),
                ('currLink', models.CharField(blank=True, max_length=255)),
                ('cOrder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255)),
                ('gradDate', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=255)),
                ('eOrder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PastProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastName', models.CharField(max_length=255)),
                ('pastDesc', models.CharField(max_length=255)),
                ('pastImg', models.CharField(max_length=255)),
                ('pastSource', models.CharField(blank=True, max_length=255)),
                ('pastLink', models.CharField(blank=True, max_length=255)),
                ('pOrder', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Updated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whyUpdate', models.CharField(max_length=255)),
                ('updateType', models.IntegerField(choices=[{'id': 0, 'updateType': 'Current'}, {'id': 1, 'updateType': 'Past'}, {'id': 2, 'updateType': 'All'}, {'id': 3, 'updateType': 'Resume'}, {'id': 4, 'updateType': 'Contact'}], default=0)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('dates', models.CharField(max_length=255)),
                ('jobDesc01', models.CharField(max_length=100)),
                ('jobDesc02', models.CharField(blank=True, max_length=100)),
                ('jobDesc03', models.CharField(blank=True, max_length=100)),
                ('jobDesc04', models.CharField(blank=True, max_length=100)),
                ('wOrder', models.IntegerField()),
            ],
        ),
    ]
