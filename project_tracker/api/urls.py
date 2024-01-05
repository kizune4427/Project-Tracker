from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('cards/', views.get_cards, name='cards'),
    path('cards/<str:pk>/', views.get_card, name='card'),
]
