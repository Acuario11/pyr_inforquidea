from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated, #si esta autenticado
    IsAdminUser, #si es admin
    AllowAny, #cualquier usuario
)

from . import serializers
from . import models


class ViveroViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = serializers.ViveroSerializer
    queryset = models.Vivero.objects.all()
    