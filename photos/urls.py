from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.single, name='single'),
    path('',views.index, name='index'),
]