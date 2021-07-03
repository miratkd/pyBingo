from django.urls import path, include
from bingoApp import views
from rest_framework.routers import DefaultRouter
from bingoApp.views import BingoAdminViewSet

router = DefaultRouter()
router.register(r'bingo_admin', BingoAdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
