from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class PickupPoint(models.Model):
    postal_code = models.IntegerField()
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    building = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pickup_point'

    def __str__(self) -> str:
        return f'Пункт выдачи заказов по адресу: {self.postal_code} г. {self.city}, ул. {self.street}, д. {self.building}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self) -> str:
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producer'

    def __str__(self) -> str:
        return self.name



class Provider(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'provider'

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'type'

    def __str__(self) -> str:
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'unit'

    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'

    def __str__(self) -> str:
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, patronymic=None, password=None, role=None):
        if not email:
            raise ValueError('Email обязателен')
        if not password:
            raise ValueError('Пароль обязателен')
        if not first_name:
            raise ValueError('Имя обязательно')
        if not last_name:
            raise ValueError('Фамилия обязательна')

        if role is None:
            role = Role.objects.get(name='Авторизированный клиент')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, patronymic=None, password=None):
        admin_role = Role.objects.get(name='Администратор')
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            password=password,
            role=admin_role,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='role_id', related_name='users')
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        full_name = f'{self.last_name} {self.first_name}'
        if self.patronymic:
            full_name += f' {self.patronymic}'
        return f'{full_name} ({self.role})'


class Product(models.Model):
    article = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='products')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
    
    @property
    def discounted_price(self):
        return round(self.price * (100 - self.discount) / 100, 2)

    def __str__(self) -> str:
        return f'Артикул: {self.article}, Наименование: {self.type}, Категория: {self.category}, цена: {self.price}, остаток: {self.stock} {self.unit}'


class Order(models.Model):
    created_at = models.DateField()
    delivered_at = models.DateField()
    pickup_point_address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    receipt_code = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        managed = False
        db_table = 'order'
        
    @property
    def total(self):
        return sum(item.product.discounted_price for item in self.products_in_order.all()) # type: ignore

    def __str__(self) -> str:
        return f'Заказ от {self.created_at}, статус: {self.status}, дата доставки: {self.delivered_at}, сделан пользователем: {self.user}.'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products_in_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_in_order')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_in_order'

    def __str__(self) -> str:
        return f'Заказ: {self.order}, Товар: {self.product}, Количество: {self.amount}'