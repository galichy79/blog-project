##### Создаем приложение блог


```python
python3 manage.py startapp blog
``` 

Cоздаем приложение events
```python 
python3 manage.py startapp events
``` 

Модель - это класс. Мы должны создать здесь класс.


[Models в документации ImageField](https://docs.djangoproject.com/en/4.1/ref/models/fields/)

migrations - способ в джанго обновлять базу данных

```python 
python3 manage.py migrate
```

Прописываем в settings.py 'events.apps.EventsConfig'

```python 
python3 manage.py makemigrations
```

```python 
python3 -m pip install Pillow
```

Применяем обновление
```python 
python manage.py migrate 
```

77. Admin

```python
 python manage.py createsuperuser
 ``` 

  
 [как разрешить windows 10 скачивать файлы из неизвестных источников](https://www.youtube.com/watch?v=8mdWNF7jkDA)

 После установки постгрескл запустить SQL shell

 80. Подключаем PostgreSQL к проекту.

 Устанавливаем пароль юзера постгрес

 ```bash
 \password postgres
 ``` 

 [create .gitignore](https://www.toptal.com/developers/gitignore/)


Запускаем постгрес 

```bash
sudo -i -u postgres
```

```bash
psql
```

To exit

```bash
 \q
 ```

Посмотреть всех пользователей БД
```bash
\du 
```

Установить пароль для пользователя postgres
```bash
\password postrges 
```

```bash
CREATE DATABASE blogdb;
```
Создаем суперюзера для админки:
```bash
python3 manage.py createsuperuser
``` 

```python 
python3 manage.py makemigrations
```

```python
python3 manage.py migrate
```

responsive - адаптивный

[Bootstrap 5 Tutorial](https://www.w3schools.com/bootstrap5/index.php)

85. Bootstrap. Часть 2
86. Bootstrap. Часть 3
88. Задание 2. Решение
89. Отображение объектов Event
91. Задание 3





