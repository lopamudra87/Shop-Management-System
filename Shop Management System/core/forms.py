from django import forms
from .models import Product, Customer, Supplier, Purchase, Sale

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'sku', 'description', 'stock', 'price', 'is_active']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'city']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'city']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier', 'reference']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'reference']
