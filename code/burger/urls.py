from django.urls import path
from burger import views

urlpatterns = [

path('',views.index, name='index'),
path('findRestaurant',views.findRestaurant, name = 'findRestaurant')


]