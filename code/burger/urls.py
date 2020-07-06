from django.urls import path
from burger import views

urlpatterns = [

path('',views.index, name='index')

]