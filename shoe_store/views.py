from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from pathlib import Path
from shoe_store.settings import BASE_DIR
from shoe_store.models import Product, Order
from shoe_store.forms import SignUpForm, ProductForm, OrderForm


templates = Path(BASE_DIR) / 'templates'


def is_admin(user):
    return user.role.name == 'Администратор'


def is_manager(user):
    return user.role.name == 'Менеджер'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('products')


@login_required
def products_page(request):
    html_file = templates / 'products.html'
    products = Product.objects.all()
    
    context = {
        'title': 'Товары',
        'products': products,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, html_file.as_posix(), context)


@login_required
@user_passes_test(is_admin)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'title': 'Добавить товар'})


@login_required
@user_passes_test(is_admin)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'title': 'Редактировать товар'})


@login_required
@user_passes_test(is_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


@login_required
def orders_page(request):
    html_file = templates / 'orders.html'

    orders = Order.objects.all() if request.user.is_staff else Order.objects.filter(user=request.user)
    title = 'Заказы' if request.user.is_staff else 'Мои Заказы'
    
    context = {
        'title': title,
        'is_admin': is_admin(request.user),
        'orders': orders,
    }
    return render(request, html_file.as_posix(), context)


@login_required
@user_passes_test(is_admin)
def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form, 'title': 'Добавить заказ'})


@login_required
@user_passes_test(is_admin)
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form, 'title': 'Редактировать заказ'})


@login_required
@user_passes_test(is_admin)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orders')
