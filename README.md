## REST API для Федерации Спортивного Туризма России

API приложения Федерации Спортивного Туризма России с помощью Django Rest Framework. 
http://51.250.121.9:8000/submitData/

Также чтобы ознакомиться с методами API можно воспользоваться Swagger UI
http://51.250.121.9:8000/swagger/

### Описание проекта

Для пользователя в приложении будет доступно:

- Внесение информации о новом объекте.

- Редактирование в приложении неотправленных на сервер ФСТР данных об объектах. На перевале не всегда работает Интернет.

- Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим их автозаполнением при внесении данных о новых объектах.

Отправка данных на сервер ФСТР.

- Получение уведомления о статусе отправки (успешно/неуспешно).

Пользователь с помощью приложения также будет передавать в ФСТР следующие данные:

- имя пользователя

- почта и телефон пользователя

- координаты перевала и его высота

- название объекта

- сложность прохождения

- добавление фотографий объекта

### Описание эндпоинтов 

HTTP request | Description
 ------------- | -------------
 /submitData | Получить список всех объявлений
 /submitData/submit/ | Создание объявлений в json формате
 /api/submitData/create/ |  Создание объявлений с помощью браузерной формы
 /submitData/<id>/ | Получить объявление по id
 /submitData/<id>/update/ | Обновить/редактировать объявление в json формате
 /api/submitData/<id>/update/ | Обновить/редактировать объявление с помощью браузерной формы
 /submitData/upload/ | Загрузить фото
 /swagger/ | Получить автодокументацию приложения с помощью SWAGGER


### Методы API

##### Метод **POST** /submitData/submit/

Пример **POST** запроса JSON:

```JSON
{
            "user": {
                "name": "James",
                "second_name": "Howard",
                "last_name": "Newman",
                "phone": "+1345987349",
                "email": "user@example.com"
            },
            "levels": {
                "winter": "Hard",
                "summer": "Hard",
                "autumn": "Hard",
                "spring": "Hard"
            },
            "coordinates": {
                "latitude": 535.0,
                "longitude": 23.0,
                "height": 534
            },
            "status": "New",
            "beauty_title": "Increadible!",
            "connect": "Yes",
            "title": "The best mountain",
            "other_titles": "No title"
        }
```

Допустимые значения поля status:

'new' - новая заявка(default-значение);
'pending' — на рассмотрении;
'accepted' — заявка принята;
'rejected' — заявка отклонена.

##### Метод GET /submitData/
Этот метод получает список всех созданных объявлений.

##### Метод GET /submitData/<id>/
Этот метод получает по id всю информацию об указанном объявлении.

Пример **GET** запроса JSON:

```JSON
{
            "id": 1,
            "user": {
                "name": "James",
                "second_name": "Howard",
                "last_name": "Newman",
                "phone": "+1345987349",
                "email": "user@example.com"
            },
            "levels": {
                "winter": "Hard",
                "summer": "Hard",
                "autumn": "Hard",
                "spring": "Hard"
            },
            "coordinates": {
                "latitude": 535.0,
                "longitude": 23.0,
                "height": 534
            },
            "add_time": "2023-07-18T11:44:22.502615Z",
            "status": "New",
            "beauty_title": "Increadible!",
            "connect": "Yes",
            "title": "The best mountain",
            "other_titles": "No title"
        }
```

##### Метод PATCH /submitData/<id>/update/
Позволяет отредактировать существующее объявление, если оно в статусе `new`. При этом редактировать можно все поля, кроме ФИО, адреса почты и номера телефона. В качестве результата изменения приходит ответ следующего содержания:

state:
0 — изменить объявление не удалось
1 — внесение изменений в базе данных прошло успешно

Примеры ответов JSON:
```JSON
{"state": 0, "message": "Mountain does not exist"}
{"state": 0, "message": "Mountain status is not New"}
{"state": 1, "message": "Данные успешно обновлены"}
```

##### Метод GET+email /submitData/?user_email=email

Возвращает данные всех объектов, отправленных на сервер пользователем с почтой email. 

Пример запроса:

GET /submitData/?user_email=user@example.com


В ходе создания проекта использовались технологии:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

