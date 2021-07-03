from django.shortcuts import render
from rest_framework import viewsets
from bingoApp.models import BingoAdmin, AdminNumber
from bingoApp.serializers import BingoAdminSerializer, AdminNumberSerializer
from rest_framework.response import Response



class BingoAdminViewSet(viewsets.ModelViewSet):
    queryset = BingoAdmin.objects.all()
    serializer_class = BingoAdminSerializer


class AdminNumberViewSet(viewsets.ModelViewSet):
    queryset = AdminNumber.objects.all()
    serializer_class = AdminNumberSerializer

    def create(self, request):
        admin_id = request.query_params['admin_id']
        print(admin_id)
        response = AdminNumberSerializer.create(self, admin_id=admin_id)
        return Response(response.data)
