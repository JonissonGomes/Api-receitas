from django.db import models
from uuid import uuid4

class Receitas(models.Model):
    id_receita = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    ingredientes = models.CharField(max_length=255)
    modo = models.CharField(max_length=255)
    tempo = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)