from django.urls import path 
from .views import MenuItemView, SingleMenuItemView,msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path('api/menu-items/',MenuItemView.as_view()),
path('api/menu-items/<int:pk>/', SingleMenuItemView.as_view()),
path('api/msg',msg),
path('obtain-token/',obtain_auth_token),
]