# Generated by Django 4.2.1 on 2023-05-29 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man_shop', '0002_remove_clothingitem_vid_clothingitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingitem',
            name='image',
            field=models.ImageField(null=True, upload_to='clothing_images'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Ваш отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name_reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='man_shop.clothingitem')),
            ],
        ),
    ]
