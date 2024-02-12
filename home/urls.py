from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'), 
]