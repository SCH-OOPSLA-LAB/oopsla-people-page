# Generated by Django 4.2.4 on 2023-08-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeminarPPT',
            fields=[
                ('uploadDate', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('people', models.CharField(max_length=50)),
                ('pptFile', models.FileField(upload_to='')),
                ('pptFileName', models.CharField(max_length=50)),
            ],
        ),
    ]
