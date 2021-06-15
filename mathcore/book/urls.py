from django.urls import path, include
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.bookprint, name='print'),
    path('booklist/', views.booklist)
]