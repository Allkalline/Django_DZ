from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('list_ordered/<int:client_id>/', views.list_ordered, name='list_ordered'),
    path('add_product/', views.add_product, name='add_product'),
]