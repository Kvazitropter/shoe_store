from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from shoe_store.models import User, Role, Product, Order


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=255, widget=forms.EmailInput(attrs={'autofocus': True}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'


class SignUpForm(UserCreationForm):
    patronymic = forms.CharField(
        max_length=255,
        required=False,
        label='Отчество'
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget = forms.TextInput(attrs={'autofocus': True})

        self.fields['email'].label = 'Email'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже существует.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        default_role = Role.objects.get(name='Авторизированный клиент')
        user.role = default_role
        if commit:
            user.save()
        return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'article': 'Артикул',
            'type': 'Наименование',
            'unit': 'Единица измерения',
            'price': 'Цена',
            'provider': 'Поставщик',
            'producer': 'Производитель',
            'category': 'Категория',
            'discount': 'Скидка',
            'stock': 'Остаток',
            'description': 'Описание',
            'photo': 'Фото',
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'delivered_at': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'created_at': 'Дата создания',
            'delivered_at': 'Дата доставки',
            'pickup_point_address': 'Адрес пвз',
            'user': 'Получатель',
            'receipt_code': 'Код получения',
            'status': 'Статус',
        }
