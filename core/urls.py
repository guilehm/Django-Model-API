from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('api/', views.api, name='api'),
    path('api/products/<str:product_slug>/', views.ProductDetail.as_view(), name='product_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)