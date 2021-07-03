from rest_framework import serializers
from bingoApp.models import BingoAdmin


class BingoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = BingoAdmin
        fields = ['id', 'name']
