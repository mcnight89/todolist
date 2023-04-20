# ToDo

    Приложение для отслеживания выполнения задач

Стек технологий
    
    python==3.10
    Django==4.1.7
    Postgres

Виртуальное окружение

    1. Создание окружения - python -m venv venv
    2. Активация виртуального окружения - source venv/bin/activate
    3. Выход из виртуального окружения - deactivate

Установка зависимостей

    pip install -r requirements.txt

POSTGRES

    docker images | grep postgres - postgres latest version
    docker-compose config - конфигурация 

Запуск и просмотр запущенной базы

    docker-compose up -d db - запуск    
    docker-compose ps -a - просмотр

Миграции

    ./manage.py makemigrations --dry-run - что произайдет, если мы сделаем миграцию
    ./manage.py makemigrations- создаем миграции
    ./manage.py migrate - накатываем миграции

Runserver

    python manage.py runserver
