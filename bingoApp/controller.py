from bingoApp import models
from bingoApp import serializers


def clear_all_numbers(admin_id):
    admin = models.BingoAdmin.objects.get(id=admin_id)
    for number in admin.numbers.all():
        number.delete()


def toggle_bingo(card_id):
    card = models.Card.objects.get(id=card_id)
    card.is_bingo = not card.is_bingo
    if card.is_bingo:
        models.BingoNotification.objects.create(admin=card.admin, card=card)
    card.save()
    return serializers.CardSerializer(card)


def get_notification(admin_id):
    notification_list = models.BingoNotification.objects.filter(admin__id=admin_id, is_visualized=False)
    for notification in notification_list:
        notification.is_visualized = True
        notification.save()
    return serializers.BingoNotificationSerializer(notification_list, many=True)

