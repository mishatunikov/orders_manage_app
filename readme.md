# Orders_manage_app

Orders_manage_app - это веб-приложение для управления заказами. Позволяет пользователям добавлять, удалять, искать и изменять статусы заказов.

## Описание

Функционал:
- Добавление заказа: Пользователь может ввести номер стола и список блюд с ценами, система добавит заказ с уникальным ID, рассчитанной суммарной стоимостью и статусом "в ожидании".
- Удаление заказа: Пользователь может выбрать заказ по ID и удалить его из системы.
- Редактирование заказа: Пользователь может выбрать заказ по ID и отредактировать его статус, состав, номер стола.
- Поиск заказа: Поиск заказов по номеру стола или статусу через поисковую строку.
- Отображение всех заказов: Главная страница отображает все заказы с их описанием в порядке создания (выше самые новые).
- Отдельная страница заказа: Отдельная страница позволяет посмотреть более подробное описание заказа - увидеть цену каждого из блюд по отдельности.
- Отдельная страница для просмотра статистики работы: Отдельная страница, которая включает данные о количестве заказов с разным статусом, а также суммарной выручки за оплаченные заказы.

## Установка и запуск

Для установки и запуска проекта "Orders_manage_app" выполните следующие шаги:

1. Склонировать репозиторий:
    `https://github.com/mishatunikov/orders_manage_app.git`


2. Создать и активировать виртуальное окружение:

    Создать:
    - macOS/Linux
    `python -m venv venv`

    - Windows
    `python -m venv venv`

    Активировать:
    - macOS/Linux
    `source venv/bin/activate`

    - Windows
    `source venv\Scripts\activate`
    

3. Установить зависимости:
    
    `pip install -r requirements.txt`
    

4. Применить миграции базы данных:
    
    `python manage.py migrate`
    

5. Запустить сервер разработки:
    
    `python manage.py runserver`
    
Перейти по адресу http://127.0.0.1:8000/ для доступа к проекту.

Дополнительно:

1. Для управления панелью администратора создайте пользователя:
`python manage.py createsuperuser`

`http://127.0.0.1:8000/admin/ перейдите по адресу и авторизуйтесь.`

2. Если хотите посмотреть сайт с небольшим наполнением загрузите фикстуры:
`python manage.py loaddata db.json `
