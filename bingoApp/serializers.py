import random

from rest_framework import serializers
from bingoApp.models import BingoAdmin, AdminNumber, Card, BingoNotification


class BingoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = BingoAdmin
        fields = ['id', 'name']

    def get_all_cards(id):
        admin = BingoAdmin.objects.get(id=id)
        return CardSerializer(admin.cars, many=True)


class AdminNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNumber
        fields = ['number']
        depth = 1

    def create(self, admin_id):
        admin = BingoAdmin.objects.get(id=admin_id)
        number_list = AdminNumber.objects.filter(admin=admin)
        numbers = []
        for x in number_list:
            numbers.append(x.number)
        if len(numbers) < 99:
            while True:
                random_number = random.randint(0, 99)
                if random_number not in numbers:
                    number = AdminNumber.objects.create(number=random_number, admin=admin)
                    return AdminNumberSerializer(number)
        else:
            raise Exception

    def retrieve(self, admin_id):
        admin = BingoAdmin.objects.get(id=admin_id)
        response = AdminNumber.objects.filter(admin=admin)
        return AdminNumberSerializer(response, many=True)


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'is_bingo', 'admin', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11',
                  'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25']

    def create(self, validate_data):
        data = validate_data
        numbers_list = []
        i = 0
        while i < 25:
            repeat = True
            while repeat:
                random_number = random.randint(1, 99)
                if random_number not in numbers_list:
                    numbers_list.append(random_number)
                    repeat = False
            i += 1

        admin = BingoAdmin.objects.get(id=data['admin'])
        card = Card.objects.create(
            name=data['name'],
            admin=admin,
            p1=numbers_list[0],
            p2=numbers_list[1],
            p3=numbers_list[2],
            p4=numbers_list[3],
            p5=numbers_list[4],
            p6=numbers_list[5],
            p7=numbers_list[6],
            p8=numbers_list[7],
            p9=numbers_list[8],
            p10=numbers_list[9],
            p11=numbers_list[10],
            p12=numbers_list[11],
            p13=numbers_list[12],
            p14=numbers_list[13],
            p15=numbers_list[14],
            p16=numbers_list[15],
            p17=numbers_list[16],
            p18=numbers_list[17],
            p19=numbers_list[18],
            p20=numbers_list[19],
            p21=numbers_list[20],
            p22=numbers_list[21],
            p23=numbers_list[22],
            p24=numbers_list[23],
            p25=numbers_list[24],
        )
        return CardSerializer(card)


class BingoNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BingoNotification
        fields = ['card']
        depth = 1
