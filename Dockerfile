# 1. Берем основу (Python)
FROM python:3.10-slim

# 2. Установка переменных окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 3. Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# 4. Создаем папку для проекта внутри Докера
WORKDIR /app

# 5. Копируем список библиотек
COPY Love/requirements.txt .

# 6. Устанавливаем их
RUN pip install --no-cache-dir -r requirements.txt

# 7. Копируем все наши файлы проекта
COPY . .

# 8. Собираем статические файлы (если нужно)
RUN cd Love && python manage.py collectstatic --noinput || true

# 9. Открываем порт
EXPOSE 8000

# 10. Запускаем миграции и сервер
ENTRYPOINT ["sh", "-c", "cd Love && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]