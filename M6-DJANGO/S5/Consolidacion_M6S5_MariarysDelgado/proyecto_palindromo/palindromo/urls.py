from django.urls import path
from . import views

urlpatterns = [
    path('verificar/<str:palabra>/', views.verificar_palindromo, name='verificar_palindromo'),
]