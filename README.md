# Yandex Afisha
Это проект Django, разработанный пользователем 5nail000. Он представляет собой онлайн-платформу, похожую на Яндекс.Афишу.

## Начало работы
Для запуска локальной копии следуйте этим простым шагам.

## Предварительные условия
Этот проект использует Python 3.11 и Django. Убедитесь, что у вас на компьютере установлена последняя версия Python. Его можно скачать с официального сайта Python.

## Установка
* Клонируйте репозиторий:
```bash
git clone https://github.com/5nail000/django_01_yandex_afisha.git
```
* Перейдите в директорию проекта:
```bash
cd django_01_yandex_afisha
```
* Установите необходимые пакеты с помощью pip:
```bash
pip install -r requirements.txt
```
* Запустите сервер Django:
```bash
python manage.py runserver
```

Теперь можно видеть, как проект работает по адресу [localhost:8000](http://localhost:8000) в вашем веб-браузере.  
Пример проекта также доступен по адресу: [https://snail000.pythonanywhere.com/](https://snail000.pythonanywhere.com/)  
В т.ч. админка: [https://snail000.pythonanywhere.com/admin](https://snail000.pythonanywhere.com/admin)  
Логин/пароль администратора: **adm**/**adm**


## Структура проекта
Проект состоит из нескольких директорий и файлов:
* media/place_images: Эта директория содержит статические изображения, используемые в проекте.
* static: Эта директория содержит статические файлы, такие как CSS и JavaScript файлы.
* templates: Эта директория содержит HTML шаблоны.
* where_to_go_app: Эта директория содержит приложение Django.
* yandex_afisha: Эта директория содержит файлы настроек и конфигурации для проекта Django.
* .gitignore: Этот файл определяет, какие файлы и директории следует игнорировать в git.
* manage.py: Это утилита командной строки, которая позволяет взаимодействовать с этим проектом Django.
* requirements.txt: Этот файл содержит список элементов для установки с помощью pip install.

## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
