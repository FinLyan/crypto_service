# crypto_pet — веб-сервис шифрования

Учебный пет-проект: REST-сервис шифрования/дешифрования текста четырьмя шифрами
(Цезарь, Виженер, XOR, Fernet) с единым контрактом ядра, историей операций и тестами.

## Стек

Python 3.13 · Django + DRF · cryptography · pytest / pytest-django · SQLite (MVP)

## Что внутри

- `crypto_core/` — ядро, независимое от Django: базовый контракт `BaseCipher`,
  реестр шифров, доменные исключения, адаптер Fernet поверх библиотеки `cryptography`;
- `api/` — Django-приложение: REST-эндпоинты, модель истории операций, админка;
- `tests/` — 38 тестов: алгоритмы шифров, контракт ядра, API-эндпоинты.

## API

| Метод | URL                  | Описание                          |
|-------|----------------------|-----------------------------------|
| GET   | /api/v1/ciphers/     | список шифров с метаданными       |
| POST  | /api/v1/encrypt/     | зашифровать текст                 |
| POST  | /api/v1/decrypt/     | расшифровать текст                |
| GET   | /api/v1/history/     | лента успешных операций           |

Пример:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/encrypt/ \
  -H "Content-Type: application/json" \
  -d "{\"cipher\": \"caesar\", \"key\": \"3\", \"text\": \"abc\"}"
```

Ответ: `{"result": "def"}`. Ошибки входа возвращают HTTP 400 с телом `{"error": "..."}`.

## Запуск

```bash
git clone <ссылка на репозиторий>
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Тесты

```bash
python -m pytest -q
```

## Ограничения

- нет аутентификации — история публична и носит демонстрационный характер;
- SQLite вместо Postgres.

## Roadmap

- эндпоинт криптоанализа для шифров с малым пространством ключей;
- расширение реестра новыми шифрами.