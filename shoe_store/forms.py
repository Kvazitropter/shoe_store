from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from shoe_store.models import User, Role, Product, Order


required_error_message = {
    'required': 'Поле не может быть пустым'
}

email_error_messages = {
    **required_error_message,
    'invalid': 'Введеный email некорректен',
}

password_error_messages = {
    'password_too_short': 'Минимальная длина пароля - 6 символов',
    'password_entirely_numeric': 'Пароль не может состоять только из цифр',
    'password_too_similar': 'Пароль слишком похож на вашу личную информацию',
    'password_mismatch': 'Пароли не совпадают'
}

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        max_length=255,
        widget=forms.EmailInput(attrs={'autofocus': True}),
        error_messages=email_error_messages
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].label = 'Пароль'

        self.error_messages = {
            'password': required_error_message,
            'invalid_login': 'Неверный логин или пароль',
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        error_messages=email_error_messages,
    )
    patronymic = forms.CharField(
        max_length=255,
        required=False,
        label='Отчество',
        error_messages=required_error_message,
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget = forms.TextInput(attrs={'autofocus': True})

        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        self.error_messages = {
            'email': email_error_messages,
            'first_name': required_error_message,
            'last_name': required_error_message,
            'password1': {
                **required_error_message,
                **password_error_messages,
            },
            'password2': {
                **required_error_message,
                **password_error_messages,
            },
        }

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
    photo = forms.ImageField(required=False)   

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {
            'article': required_error_message,
            'type': required_error_message,
            'unit': required_error_message,
            'price': required_error_message,
            'provider': required_error_message,
            'producer': required_error_message,
            'category': required_error_message,
            'discount': required_error_message,
            'stock': required_error_message,
            'description': required_error_message,
            'photo': {},
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('created_at', 'delivered_at', 'pickup_point_address', 'receipt_code', 'status')
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'delivered_at': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'created_at': 'Дата создания',
            'delivered_at': 'Дата доставки',
            'pickup_point_address': 'Адрес пвз',
            'receipt_code': 'Код получения',
            'status': 'Статус',
        }
