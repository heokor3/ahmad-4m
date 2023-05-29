from django.urls import path
from . import views

app_name = 'man_shop'

urlpatterns = [
    path('', views.clothing_list, name='clothing_list'),
    path('clothing_details/<int:item_id>/', views.clothing_details, name='clothing_details'),
    path('item_detail/<int:id>/delete/', views.delete_item_list, name='item_delete'),
    path('item_detail/<int:id>/update/', views.update_item_list, name='item_update'),
    path('add-item/', views.create_item_list, name='create_item'),
]

