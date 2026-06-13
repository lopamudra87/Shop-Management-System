from django.contrib import admin
from .models import Category, Product, Customer, Supplier, Purchase, PurchaseItem, Sale, SaleItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock', 'price', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city')
    search_fields = ('name', 'email', 'phone')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city')
    search_fields = ('name', 'email', 'phone')

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'reference', 'created_at', 'total_amount')
    inlines = [PurchaseItemInline]
    search_fields = ('reference', 'supplier__name')

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('customer', 'reference', 'created_at', 'total_amount')
    inlines = [SaleItemInline]
    search_fields = ('reference', 'customer__name')
