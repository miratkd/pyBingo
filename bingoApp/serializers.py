from rest_framework import serializers
from bingoApp.models import BingoAdmin, AdminNumber


class BingoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = BingoAdmin
        fields = ['id', 'name']


class AdminNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNumber
        fields = ['number']

    def create(self, admin_id):
        admin = BingoAdmin.objects.get(id=admin_id)
        number = AdminNumber.objects.create(number=1, admin=admin)
        return AdminNumberSerializer(number)
