from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum, F

from .forms import CustomerForm, ProductForm, SupplierForm
from .models import Customer, Product, Supplier, Sale, Purchase


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password')
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    total_products = Product.objects.filter(is_active=True).count()
    total_customers = Customer.objects.count()
    total_suppliers = Supplier.objects.count()
    total_sales = Sale.objects.aggregate(total=Sum(F('items__quantity') * F('items__unit_price')))['total'] or 0
    total_purchases = Purchase.objects.aggregate(total=Sum(F('items__quantity') * F('items__unit_price')))['total'] or 0
    latest_sales = Sale.objects.order_by('-created_at')[:5]
    latest_products = Product.objects.order_by('-created_at')[:5]
    context = {
        'total_products': total_products,
        'total_customers': total_customers,
        'total_suppliers': total_suppliers,
        'total_sales': total_sales,
        'total_purchases': total_purchases,
        'latest_sales': latest_sales,
        'latest_products': latest_products,
    }
    return render(request, 'core/dashboard.html', context)


@login_required
def product_list(request):
    products = Product.objects.select_related('category').all().order_by('-created_at')
    return render(request, 'core/product_list.html', {'products': products})


@login_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully')
        return redirect('product_list')
    return render(request, 'core/product_form.html', {'form': form})


@login_required
def customer_list(request):
    form = CustomerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('customer_list')
    customers = Customer.objects.all().order_by('-created_at')
    return render(request, 'core/customer_list.html', {'customers': customers, 'form': form})


@login_required
def supplier_list(request):
    form = SupplierForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Supplier added successfully')
        return redirect('supplier_list')
    suppliers = Supplier.objects.all().order_by('-created_at')
    return render(request, 'core/supplier_list.html', {'suppliers': suppliers, 'form': form})


@login_required
def sale_list(request):
    sales = Sale.objects.select_related('customer').all().order_by('-created_at')
    return render(request, 'core/sale_list.html', {'sales': sales})


@login_required
def purchase_list(request):
    purchases = Purchase.objects.select_related('supplier').all().order_by('-created_at')
    return render(request, 'core/purchase_list.html', {'purchases': purchases})


@login_required
def report_view(request):
    top_products = Product.objects.order_by('-stock')[:5]
    best_customers = Customer.objects.annotate(total_spent=Sum(F('sales__items__quantity') * F('sales__items__unit_price'))).order_by('-total_spent')[:5]
    context = {
        'top_products': top_products,
        'best_customers': best_customers,
    }
    return render(request, 'core/reports.html', context)
