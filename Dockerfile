FROM python:3.10-alpine

# установливаем переменные среды
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем обновления и необходимые модули
RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
# Обновление pip python
RUN pip install --upgrade pip
# Установка пакетов для проекта
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
WORKDIR /usr/src/app
# Удаляем зависимости билда
RUN apk del .build-deps
# Копирование проекта
COPY . .
ENTRYPOINT ["python", "manage.py"]
# Настройка записи и доступа
RUN chmod -R 777 ./

CMD ["runserver", "0.0.0.0:8000"]



