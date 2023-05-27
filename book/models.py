from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', null=True)
    description = models.TextField()
    type_book = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

