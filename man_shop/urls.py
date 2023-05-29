from django.urls import path
from . import views

app_name = 'man_shop'

urlpatterns = [
    path('', views.clothing_list, name='clothing_list'),
    path('clothing_details/<int:item_id>/', views.clothing_details, name='clothing_details'),
]