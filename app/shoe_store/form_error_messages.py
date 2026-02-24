required_message = 'Поле не может быть пустым'
min_message = 'Не достигнута минимальная длина'
max_message = 'Превышен максимальный лимит длины'

required_error_message = {
    'required': required_message
}

char_error_messages = {
    'required': required_message,
    'min_length': min_message,
    'max_length': max_message,
}

choice_error_messages = {
    'required': required_message,
    'invalid_choice': 'Выбранная опция невалидна'
}

int_error_messages = {
    'required': required_message,
    'invalid': 'Введите целое число',
    'min_value': 'Значение не может быть меньше {min_value}',
    'max_value': 'Значение не может быть больше {max_value}',
    'step_size': 'Значение должно быть кратно {step_size}',
}

decimal_error_messages = {
    'required': required_message,
    'invalid': 'Введите число',
    'min_value': 'Значение не может быть меньше {min_value}',
    'max_value': 'Значение не может быть больше {max_value}',
    'max_digits': 'Число содержит слишком много цифр',
    'max_decimal_places': 'Слишком много знаков после запятой',
    'max_whole_digits': 'Слишком много целых разрядов',
    'step_size': 'Значение должно быть кратно {step_size}',
}

date_error_messages = {
    'required': required_message,
    'invalid': 'Выбранная дата некорректна',
}

email_error_messages = {
    **char_error_messages,
    'invalid': 'Введеный email некорректен',
}

password_error_messages = {
    **char_error_messages,
    'password_too_short': 'Минимальная длина пароля - {min_value} символов',
    'password_entirely_numeric': 'Пароль не может состоять только из цифр',
    'password_too_similar': 'Пароль слишком похож на вашу личную информацию',
    'password_mismatch': 'Пароли не совпадают'
}

image_error_messages = {
    'empty': 'Файл не выбран',
    'invalid': 'Некорректный файл',
    'invalid_image': 'Некорректное изображение',
    'missing': 'Файл отсутствует',
}

login_error_messages = {
    'email': email_error_messages,
    'username': email_error_messages,
    'password': required_error_message,
    'invalid_login': 'Неверный логин или пароль',
    'inactive': 'Этот аккаунт недействителен',
}

singup_error_messages = {
    'email': email_error_messages,
    'first_name': char_error_messages,
    'last_name': char_error_messages,
    'patronymic': char_error_messages,
    'password1': password_error_messages,
    'password2': password_error_messages,
}

product_error_messages = {
    'type': choice_error_messages,
    'unit': choice_error_messages,
    'price': decimal_error_messages,
    'provider': choice_error_messages,
    'producer': choice_error_messages,
    'category': choice_error_messages,
    'discount': decimal_error_messages,
    'stock': int_error_messages,
    'description': char_error_messages,
    'photo': image_error_messages,
}

order_error_messages = {
    'created_at': date_error_messages,
    'delivered_at': date_error_messages,
    'pickup_point_address': char_error_messages,
    'status': choice_error_messages,
}
