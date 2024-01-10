from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.single, name='single'),
    path('photos/static/', views.image_view, name='image_view'),
]