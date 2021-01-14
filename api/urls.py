from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from receitas import viewsets as receitasviewsets

route = routers.DefaultRouter()

route.register(r'receitas', receitasviewsets.ReceitasViewSet, basename="Receitas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
