from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from pathlib import Path
from shoe_store.settings import BASE_DIR
from shoe_store.models import Product, Order, Provider
from shoe_store.forms import LoginForm, SignUpForm, ProductForm, OrderForm


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

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST, request.FILES)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('products')
#     else:
#         form = LoginForm()
#     context = {
#         'title': 'Авторизация',
#         'form': form,
#         'is_admin': False,
#         'is_manager': False,
#     }
#     return render(request, 'registration/login.html', context)


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('products')
#     else:
#         form = SignUpForm()
#     context = {
#         'title': 'Регистрация',
#         'form': form,
#         'is_admin': False,
#         'is_manager': False,
#     }
#     return render(request, 'registration/signup.html', context)


@login_required
def products_page(request):
    search_query = request.GET.get('search_query', '')
    selected_provider_id = request.GET.get('selected_provider_id')
    output_order = request.GET.get('output_order')
    products = Product.objects.all() \
        .filter(
            Q(article__iregex=f'(?i){search_query}') |
            Q(description__iregex=f'(?i){search_query}')
        )
    if selected_provider_id:
        products = products.filter(provider=int(selected_provider_id))
    if output_order:
        products = products.order_by(output_order)
    
    context = {
        'title': 'Товары',
        'products': products,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
        'search_query': search_query,
        'providers': Provider.objects.all(),
        'selected_provider_id': selected_provider_id,
        'output_order': output_order,
    }
    return render(request, 'products/products.html', context)


@login_required
@user_passes_test(is_admin)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context = {
        'title': 'Добавить товар',
        'form': form,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, 'products/product_form.html', context)


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
    context = {
        'title': 'Редактировать товар',
        'form': form,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, 'products/product_form.html', context)


@login_required
@user_passes_test(is_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.products_in_order.exists(): # type: ignore
        messages.error(request, 'Невозможно удалить товар, так как он присутствует в заказe')
    else:
        product.delete()
        messages.success(request, 'Товар успешно удалён')
    return redirect('products')


@login_required
def orders_page(request):
    orders = Order.objects.all() if request.user.is_staff else Order.objects.filter(user=request.user)
    title = 'Заказы' if request.user.is_staff else 'Мои Заказы'
    
    context = {
        'title': title,
        'orders': orders,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, 'orders/orders.html', context)


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
    context = {
        'title': 'Добавить заказ',
        'form': form,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, 'orders/order_form.html', context)


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
    context = {
        'title': 'Редактировать заказ',
        'form': form,
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
    }
    return render(request, 'orders/order_form.html', context)


@login_required
@user_passes_test(is_admin)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orders')
