from django.shortcuts import render
from rest_framework import viewsets
from bingoApp.models import BingoAdmin, AdminNumber, Card
from bingoApp.serializers import BingoAdminSerializer, AdminNumberSerializer, CardSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from bingoApp import controller


class BingoAdminViewSet(viewsets.ModelViewSet):
    queryset = BingoAdmin.objects.all()
    serializer_class = BingoAdminSerializer

    @action(detail=True, methods=['delete'])
    def clear_numbers(self, request, pk=None):
        controller.clear_all_numbers(pk)
        return Response(status='204')

    @action(detail=True, methods=['get'])
    def all_cards(self, request, pk=None):
        response = self.serializer_class.get_all_cards(id=pk)
        return Response(data=response.data, status='204')


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
