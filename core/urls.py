from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.index, name='produtos'),
    path('api/', views.index, name='api'),
]