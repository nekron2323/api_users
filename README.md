# api_users
## API сервис для хранения данных о пользователях


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/nekron2323/api_users.git
```

```
cd api_users/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать супер юзера:

```
python3 api_users/manage.py createsuperuser
```

Выполнить миграции:

```
python3 api_users/manage.py migrate
```

Запустить проект:

```
python3 api_users/manage.py runserver
```

Структурированное описание сервиса можно посмотреть на странице http://127.0.0.1:8000/swagger/
