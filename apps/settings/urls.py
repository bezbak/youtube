from django.urls import path
from apps.settings.views import SettingsAPIView, SettingsCreateAPIView,SettingsUpdateAPIView

urlpatterns = [
    path('', SettingsAPIView.as_view()),
    path('create/', SettingsCreateAPIView.as_view()),
    path('update/<int:pk>/', SettingsUpdateAPIView.as_view()),
]
