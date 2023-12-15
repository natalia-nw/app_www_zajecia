from django.urls import path
from . import views
from rest_framework.authtoken import views as authViews

urlpatterns = [
    path('', views.index, name='index'),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/update/<int:pk>/', views.osoba_update),
    path('osoby/delete/<int:pk>/', views.osoba_delete),
    path('osoby/add/', views.osoba_add),
    path('osoby/<str:search_string>/', views.osoba_list_zawiera),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
    path('stanowisko/<int:id>/members/', views.osoba_stanowisko),
    path('api-token-auth/', authViews.obtain_auth_token),
    path('osoby/view/', views.osoba_view),
    path('osoby/list', views.OsobaListView.as_view()),
]
