from rest_framework import viewsets
from receitas import serializers
from receitas import models

class ReceitasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReceitasSerializer
    queryset = models.Receitas.objects.all()