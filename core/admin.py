from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','quantity']
    list_filter = ['name',]
    search_fields = ['name',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)