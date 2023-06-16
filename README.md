## Blog. Educational project



python manage.py startapp blog создаем приложение blog

python manage.py startapp events создаем приложение events

Модель - это класс. Мы должны создать здесь класс.


[Models в документации ImageField](https://docs.djangoproject.com/en/4.1/ref/models/fields/)

migrations - способ в джанго обновлять базу данных

python manage.py migrate

Прописываем в settings.py 'events.apps.EventsConfig'

python manage.py makemigrations

python -m pip install Pillow

python manage.py migrate применяем обновление

77. Admin

Нужно создать admin аккаунт 

 python manage.py createsuperuser создаем суперюзера
 Имя пишем любое

  
 [как разрешить windows 10 скачивать файлы из неизвестных источников](https://www.youtube.com/watch?v=8mdWNF7jkDA)

 После установки постгрескл запустить SQL shell

 80. Подключаем PostgreSQL к проекту.

 \password postgres устанавливаем пароль юзера постгрес

 [create .gitignore](https://www.toptal.com/developers/gitignore/)


Запускаем постгре 

```sudo -i -u postgres```

```psql```

To exit

``` \q```

\du - посмотреть всех пользователей БД

\password postrges - установить пароль для пользователя postgres

CREATE DATABASE blogdb;

```python3 manage.py createsuperuser``` - создаем суперюзера для админки.

python3 manage.py makemigrations

python3 manage.py migrate

responsive - адаптивный

[Bootstrap 5 Tutorial](https://www.w3schools.com/bootstrap5/index.php)

85. Bootstrap. Часть 2
86. Bootstrap. Часть 3
88. Задание 2. Решение
89. Отображение объектов Event





