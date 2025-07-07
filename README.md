# Django Message Broadcasting with Celery and Redis

Простое Django-приложение для асинхронной рассылки сообщений с использованием Celery и Redis в Docker-контейнере.

Использование
Теперь вы можете создавать задачи по рассылке сообщений через Django Admin или API.
Также можно добавлять и сохранять email адреса, а для удаления или более точного контроля — использовать административную страницу.

## Технологический стек

- **Django** - веб-фреймворк
- **Celery** - асинхронная очередь задач
- **Redis** - брокер сообщений и бэкенд результатов
- **Docker** - контейнеризация Redis

## Установка и настройка

### Предварительные требования

- Docker (для Redis)
- Redis (через Docker)

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш_пользователь/ваш_репозиторий.git
cd ваш_репозиторий
2. Настройка виртуального окружения (рекомендуется)
bash
python -m venv venv
# Активация:
# Linux/MacOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

3. Установка зависимостей
pip install -r requirements.txt
Запуск проекта

1. Запуск Redis в Docker
docker run -d --name redis -p 6379:6379 redis:latest

2. Настройка Django
Убедитесь, что в settings.py указаны корректные настройки Celery:
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

3. Применение миграций и запуск сервера
python manage.py migrate
python manage.py runserver

4. Запуск Celery worker
В новом терминале:
# Linux/MacOS:
celery -A your_project_name worker --loglevel=info
# Windows:
celery -A your_project_name worker --loglevel=info --pool=solo
