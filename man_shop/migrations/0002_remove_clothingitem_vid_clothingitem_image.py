# Generated by Django 4.2.1 on 2023-05-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothingitem',
            name='vid',
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]