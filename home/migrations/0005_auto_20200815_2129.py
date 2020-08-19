# Generated by Django 3.1 on 2020-08-15 21:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_signup_tedxexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='signup',
            name='callnumber',
        ),
        migrations.AddField(
            model_name='signup',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d(9,15)$')]),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(help_text='enter your email', max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=56),
        ),
        migrations.CreateModel(
            name='WorkWithUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=254)),
                ('callnumber', models.IntegerField()),
                ('field', models.CharField(max_length=3000)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.degree')),
            ],
        ),
    ]