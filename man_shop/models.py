from django.db import models


class Clothingitem(models.Model):
    CATEGORY_CHOICES = (
        ('Верхняя одежда', 'Верхняя одежда'),
        ('Брюки', 'Брюки'),
        ('Обувь','Обувь')
    )

    MATERIAL_CHOICES = (
        ('Хлопок', 'Хлопок'),
        ('Деним', 'Деним'),
        ('Шерсть','Шерсть'),
    )

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothing_images', null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    def __str__(self):
        return self.name