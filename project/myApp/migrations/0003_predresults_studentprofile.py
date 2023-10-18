# Generated by Django 4.0 on 2023-10-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_account_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cet', models.FloatField()),
                ('gpa', models.FloatField()),
                ('strand', models.CharField(max_length=200)),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OAPR', models.FloatField()),
                ('SHS_Strand', models.CharField(max_length=100)),
                ('SHS_GWA', models.FloatField()),
                ('recommended_course', models.CharField(max_length=100)),
            ],
        ),
    ]
