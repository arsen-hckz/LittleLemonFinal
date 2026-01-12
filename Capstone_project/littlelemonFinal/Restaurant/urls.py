from django.urls import path 
from .views import MenuItemView

urlpatterns = [
path('api/menu',MenuItemView.as_view()),
]