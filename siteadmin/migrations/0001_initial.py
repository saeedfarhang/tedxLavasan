# Generated by Django 3.1 on 2020-08-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=500)),
                ('insta_id', models.CharField(max_length=100)),
                ('long_description', models.TextField()),
                ('site_address', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='user.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='user.png', upload_to='')),
                ('name', models.CharField(max_length=56)),
                ('title', models.CharField(max_length=56)),
                ('instagram', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
            ],
        ),
    ]
