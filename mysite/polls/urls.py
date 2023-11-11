from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoba_add/', views.osoba_add),
    path('osoby/<str:search_string>/', views.osoba_list_zawiera),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
]
