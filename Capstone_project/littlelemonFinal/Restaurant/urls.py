from django.urls import path 
from .views import MenuItemView, SingleMenuItemView,msg,restaurant_home


urlpatterns = [
path('api/menu-items/',MenuItemView.as_view()),
path('api/menu-items/<int:pk>/', SingleMenuItemView.as_view()),
path('api/msg',msg),
path('',restaurant_home),
]