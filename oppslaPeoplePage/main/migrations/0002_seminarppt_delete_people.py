# Generated by Django 4.2.4 on 2023-08-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seminarPPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDate', models.DateField(auto_created=True)),
                ('people', models.CharField(max_length=10)),
                ('pptFile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]