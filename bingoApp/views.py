from django.shortcuts import render
from rest_framework import viewsets
from bingoApp.models import BingoAdmin
from bingoApp.serializers import BingoAdminSerializer


class BingoAdminViewSet(viewsets.ModelViewSet):
    queryset = BingoAdmin.objects.all()
    serializer_class = BingoAdminSerializer

