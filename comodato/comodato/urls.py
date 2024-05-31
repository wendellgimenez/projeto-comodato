# comodato/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', include('equipamentos.urls')),
    path('', lambda request: redirect('equipamento_list')),  # Adicionar esta linha
]
