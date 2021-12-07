from bingoApp import models


def clear_all_numbers(admin_id):
    admin = models.BingoAdmin.objects.get(id=admin_id)
    for number in admin.numbers.all():
        number.delete()
