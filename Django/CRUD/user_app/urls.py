from django.urls import path
from .views import home, user_update, user_delete

urlpatterns = [
    path('', home, name='home'),
    path('update/<int:id>/', user_update, name='user_update'),
    path('delete/<int:id>/', user_delete, name='user_delete'),
]
