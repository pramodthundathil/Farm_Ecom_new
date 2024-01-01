# Generated by Django 5.0 on 2024-01-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Disease',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Disease_Discription',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Other',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Remedy',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Symptoms',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='Symptoms_Discription',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
