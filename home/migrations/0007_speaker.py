# Generated by Django 3.1 on 2020-08-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200815_2144'),
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
                ('long_description', models.CharField(max_length=1000)),
                ('site_address', models.CharField(max_length=100)),
            ],
        ),
    ]
