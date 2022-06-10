# Проект YaMDb


### Описание

Проект YaMDb собирает отзывы  пользователей на произведения.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется рейтинг произведения.

API для "YaMDb" дает возможность взаимодействоть с функциональной частью "YaMDb" через API-сервис.

### Технологии

Python 3.7

Django 2.2.19


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Kegami1/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
для Mac или Linux:
python3 -m venv env
source venv/bin/activate
```
```
для Windows:
python -m venv venv
source venv/Scripts/activate 
```

Установить зависимости из файла requirements.txt:

```
для Mac или Linux:
python3 -m pip install --upgrade pip
```
```
для Windows:
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
для Mac или Linux:
python3 manage.py migrate
```
```
для Windows:
python manage.py migrate
```

Загрузить данные из csv-файлов:
```
для Mac или Linux:
python3 manage.py load_users_data
python3 manage.py load_review_data
```
```
для Windows:
python manage.py load_users_data
python manage.py load_review_data
```

Запустить проект:

```
для Mac или Linux:
python3 manage.py runserver
```
```
для Windows:
python manage.py runserver
```


### Примеры запросов к API

# Алгоритм регистрации пользователей

Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).

Регистрация нового пользователя:

```
POST: /api/v1/auth/signup/
```
```
Тело запроса:
{
  "email": "string",
  "username": "string"
}
```
```
Ответ:
{
  "email": "string",
  "username": "string"
}
```

Получение JWT-токена:
```
POST: /api/v1/auth/token/
```
```
Тело запроса:
{
  "username": "string",
  "confirmation_code": "string"
}
```
```
Ответ:
{
  "token": "string"
}
```

Получение списка всех категорий

```
GET: /api/v1/categories/
```
```
Ответ:
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```

Добавление нового отзыва:

```
POST: /api/v1/titles/{title_id}/reviews/
```
```
Тело запроса:
{
  "text": "string",
  "score": 1
}
```
```
Ответ:
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

Изменение данных пользователя по username:


```
PATCH: /api/v1/users/{username}/
```
```
Тело запроса:
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
```
Ответ:
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


### Авторы

Белобородова Анастасия  beloborodova.anastasiia@yandex.ru

Ватагин Алексей  summer-vatagin@yandex.ru

Князев Сергей  Knyazevso@mail.ru


