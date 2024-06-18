# Generated by Django 5.0.6 on 2024-06-17 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DataRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataupload.fileupload')),
            ],
        ),
    ]