from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
    path('user/add/', views.user_create, name='user_create'),
    path('user/<int:id>/edit/', views.user_update, name='user_update'),
    path('user/<int:id>/delete/', views.user_delete, name='user_delete'),
]
