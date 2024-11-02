# models.py
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} - {self.name}"

class Livros(models.Model):
    streaming_choices = (
        ('AK', 'Amazon Kindle'),
        ('FI', 'Físico'),
    )
    name = models.CharField(max_length=50)
    streaming = models.CharField(max_length=2, choices=streaming_choices)
    note = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    categorie = models.ManyToManyField(Categories)  # Corrigido para "categorie"

    def __str__(self):
        return f"{self.id} - {self.name}"
