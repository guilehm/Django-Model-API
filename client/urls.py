from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)