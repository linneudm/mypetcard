# Generated by Django 4.2.2 on 2023-06-19 11:47

from django.db import migrations, models
import pet.models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deworkming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('date', models.DateField()),
                ('doctor_name', models.CharField(max_length=155)),
                ('crmv', models.CharField(blank=True, max_length=155, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=pet.models.vaccine_directory_path)),
            ],
        ),
        migrations.AlterField(
            model_name='petowner',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
