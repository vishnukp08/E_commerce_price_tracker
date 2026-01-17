from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_price', 'last_price', 'created_at')
    search_fields = ('name',)
