from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacto/<int:pk>/', views.DetailView.as_view(), name='detail'),
]