from django.urls import path, include
from bingoApp import views
from rest_framework.routers import DefaultRouter
from bingoApp.views import BingoAdminViewSet, AdminNumberViewSet, CardViewSet, BingoNotificationViewSet

router = DefaultRouter()
router.register(r'bingo_admin', BingoAdminViewSet)
router.register(r'admin_number', AdminNumberViewSet)
router.register(r'card', CardViewSet)
router.register(r'bingo_notification', BingoNotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
