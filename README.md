Пример приложения Flask + Redis на Docker Compose с нестандартным путём к compose-файлу, которое можно развернуть в Timeweb Cloud Apps.

🚀 [Создать свой Apps](https://timeweb.cloud/my/apps/create)

📚 [Документация Timeweb Cloud Apps](https://timeweb.cloud/docs/apps)

## Путь к compose-файлу

Compose-файл лежит не в корне репозитория:

```
services/flask-counter/compose.yml
```

При создании приложения укажите этот путь в настройках Docker Compose.

Все относительные пути в compose-файле (`build.context`, `dockerfile`, `env_file`) считаются от папки `services/flask-counter/` и должны оставаться внутри неё.

## Проверка выбора compose-файла

Рядом с `compose.yml` лежит ловушка `docker-compose.yml`. Приложение показывает на главной странице, из какого compose-файла оно запущено.

| Путь в настройках | Ожидаемый compose-файл |
|---|---|
| `services/flask-counter/compose.yml` | `compose.yml` |
| `services/flask-counter` (папка) | `docker-compose.yml` |
| не указан | `docker-compose.yml` |

Без явного пути к файлу платформа берёт `docker-compose.yml`: среди стандартных имён у него наивысший приоритет. Сам `docker compose`, запущенный в этой папке без `-f`, наоборот выберет `compose.yml`.

## Структура

```
services/flask-counter/
├── compose.yml            # web (Flask + gunicorn) и redis
├── docker-compose.yml     # ловушка для проверки выбора compose-файла
├── config/web.env         # переменные окружения web
├── docker/web.Dockerfile  # образ web, контекст сборки — services/flask-counter
└── src/
    ├── app.py
    └── requirements.txt
```

## <a name="dev"></a>Локальный запуск проекта

```bash
docker compose -f services/flask-counter/compose.yml up --build
```

Приложение откроется на http://localhost:8000, проверка состояния — http://localhost:8000/health.
