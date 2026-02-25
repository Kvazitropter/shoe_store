### Подготовка

#### Установка зависимостей и создание файла с переменными окружения

```bash
cd app
make install
```

#### Создание базы данных

Создать базу данных и запустить скрипт scriptdb.sql, добавить данные о базе данных в .env

#### Захэшировать все пароли импортированных пользователей

```bash
make console
```
`В консоли:`
```bash
from shoe_store.models import User
for user in User.objects.all():
    if not user.password.startswith('pbkdf2_sha256'):
        user.set_password(user.password)
        user.save()
```

#### Генерация ключа и добавление в файл .env

```bash
make console
```
`В консоли:`
```bash
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
`Вставить ключ в .env`

#### Запуск приложения

```bash
make dev
```
