from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from shoe_store.models import *


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    ...


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    ...


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    ...


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    ...


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    ...


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    ...


# class CustomUserAdmin(UserAdmin):
#     model = User
#     fieldsets = list(UserAdmin.fieldsets) + [
#         ('Отчество', {'fields': ('patronymic')}),
#         ('Роль', {'fields': ('role')}),
#     ]
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Отчество', {'fields': ('patronymic')}),
#         ('Роль', {'fields': ('role')}),
#     )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    ...