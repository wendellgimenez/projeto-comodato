# equipamentos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipamento_list, name='equipamento_list'),
    path('novo/', views.equipamento_create, name='equipamento_create'),
]
