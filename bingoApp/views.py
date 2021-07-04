from django.shortcuts import render
from rest_framework import viewsets
from bingoApp.models import BingoAdmin, AdminNumber, Card
from bingoApp.serializers import BingoAdminSerializer, AdminNumberSerializer, CardSerializer
from rest_framework.response import Response


class BingoAdminViewSet(viewsets.ModelViewSet):
    queryset = BingoAdmin.objects.all()
    serializer_class = BingoAdminSerializer


class AdminNumberViewSet(viewsets.ModelViewSet):
    queryset = AdminNumber.objects.all()
    serializer_class = AdminNumberSerializer

    def create(self, request):
        admin_id = request.query_params['admin_id']
        response = AdminNumberSerializer.create(self, admin_id=admin_id)
        return Response(response.data)

    def retrieve(self, request, pk=None):
        response = AdminNumberSerializer.retrieve(self, admin_id=pk)
        return Response(response.data)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request):
        response = CardSerializer.create(self, validate_data=request.data)
        return Response(response.data)
