import random
import string
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from PIL import Image
from shoe_store.models import User, Role, Product, Order
from shoe_store.form_error_messages import *


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={'autofocus': True}),
        error_messages=login_error_messages['email']
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'

        self.error_messages = login_error_messages


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        error_messages=singup_error_messages['email']
    )
    patronymic = forms.CharField(
        max_length=255,
        required=False,
        label='Отчество',
        error_messages=singup_error_messages['patronymic']
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget = forms.TextInput(attrs={'autofocus': True})
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.error_messages = singup_error_messages

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        default_role = Role.objects.get(name='Авторизированный клиент')
        user.role = default_role
        if commit:
            user.save()
        return user


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        min_value=0,
        label='Цена',
        error_messages=product_error_messages['price']
    )
    discount = forms.DecimalField(
        min_value=0,
        max_value=100,
        label='Скидка',
        error_messages=product_error_messages['discount']
    )
    stock = forms.IntegerField(
        min_value=0,
        label='Остаток',
        error_messages=product_error_messages['stock']
    )
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        required=False,
        label='Фото',
        error_messages=product_error_messages['photo'],
    )

    class Meta:
        model = Product
        fields = ('type', 'unit', 'price', 'provider', 'producer', 'category', 'discount', 'stock', 'description', 'photo')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'type': 'Наименование',
            'unit': 'Единица измерения',
            'provider': 'Поставщик',
            'producer': 'Производитель',
            'category': 'Категория',
            'description': 'Описание',
        }
        error_messages = product_error_messages

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            try:
                img = Image.open(photo)
                if img.width > 300 or img.height > 200:
                    raise ValidationError(f'Размер изображения не должен превышать 300x200')
            except Exception:
                print(Exception)
                raise ValidationError('Некорректное изображение')
        return photo
    
    def generate_unique_article(self, length=6):
        chars = string.ascii_uppercase + string.digits
        while True:
            article = ''.join(random.choices(chars, k=length))
            if not Product.objects.filter(article=article).exists():
                return article
    
    def save(self, commit=True):
        product = super().save(commit=False)
        if not product.pk:
            product.receipt_code = self.generate_unique_article()
        if commit:
            product.save()
        return product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('created_at', 'delivered_at', 'pickup_point_address', 'status')
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'delivered_at': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'created_at': 'Дата создания',
            'delivered_at': 'Дата доставки',
            'pickup_point_address': 'Адрес пункта выдачи',
            'status': 'Статус',
        }
        error_messages = order_error_messages
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        order = super().save(commit=False)
        if self.user and not order.pk:
            order.user = self.user
            while True:
                code = random.randint(100, 999)
                if not Order.objects.filter(receipt_code=code, status_id=2).exists():
                    break
            order.receipt_code = code
        if commit:
            order.save()
        return order
