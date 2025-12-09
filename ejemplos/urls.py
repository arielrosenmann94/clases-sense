from django.urls import path
from .views import calculo_iva

urlpatterns = [
    path('', calculo_iva, name='calculo_iva'),
]
