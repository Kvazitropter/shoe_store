"""
URL configuration for shoe_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from shoe_store.views import *
from shoe_store.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', products_page, name='products'),
    path('product/add/', product_add, name='product_add'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),

    path('orders/', orders_page, name='orders'),
    path('order/add/', order_add, name='order_add'),
    path('order/<int:pk>/edit/', order_edit, name='order_edit'),
    path('order/<int:pk>/delete/', order_delete, name='order_delete'),

    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
