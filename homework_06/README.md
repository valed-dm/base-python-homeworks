# Домашнее задание "Взаимодействие между контейнерами"

## Задача

- создайте docker-compose файл, настройте там связь базы данных и веб-приложения
- добавьте в свой проект модели. Это могут быть те же модели, что были использованы для сохранения данных с открытого API, это может быть и что-то новое
- добавьте возможность создавать новые записи
- создайте страницу, на которой эти записи выводятся
- база данных должна быть в отдельном контейнере
- Flask приложение должно запускаться не в debug режиме, а в production-ready (uwsgi, nginx, gunicorn)

## Критерии оценки

- docker-compose файл присутствует и работает
- приложение взаимодействует с БД
- в приложении есть возможность добавить записи, они сохраняются в БД
- в приложении есть страница, которая выдаёт доступные записи (вытаскивает из БД)
- Flask приложение настроено для запуска в production режиме (uwsgi, nginx, gunicorn)

### Запуск приложения

```code
.env.sample -> .env
SECRET_KEY=any_key_string
SESSION_TYPE=redis
CACHE_REDIS_URL=redis://0.0.0.0:6379
GOOGLE_API_KEY=AIzaSyDu7Yp0Q4DT9pGGcIx4YnVIJxeoBM6XQnI
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin_12345
POSTGRES_DB=gbooks
PGDATA=/var/lib/postgresql/data/pgdata
```

```code
docker compose up -d
```

### Adminer

```code
PostgreSQL
pg
admin
admin_12345
gbooks
```