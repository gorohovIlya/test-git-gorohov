# Сервис для магазинов

Точка входа
```
├── discount_service    #Сервис для скидок
│   ├── Dockerfile
│   ├── docs
│   │   ├── DOMAIN.md
│   │   └── SPECIFICATION.md
│   ├── Makefile
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── src
│   │   └── app
│   │       └── main.py
│   ├── tests
│   └── touch
├── docker-compose.yaml
├── order_service   #Сервис для заказов
│   ├── Dockerfile
│   ├── docs
│   │   ├── DOMAIN.md
│   │   └── SPECIFICATION.md
│   ├── Makefile
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── src
│   │   └── app
│   │       └── main.py
│   ├── tests
│   └── touch
├── PracticeMakefile
├── product_service #Сервис для товаров
│   ├── Dockerfile
│   ├── docs
│   │   ├── DOMAIN.md
│   │   └── SPECIFICATION.md
│   ├── Makefile
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── src
│   │   └── app
│   │       └── main.py
│   ├── tests
│   └── touch
├── README.md
```
## Архитектура решения

1. **Product Service** — управление каталогом товаров
2. **Discount Service** — расчет скидок на основе различных правил
3. **Order Service** — оркестрация создания заказов с интеграцией двух других сервисов

Каждый сервис работает в собственном контейнере Docker, общаясь через HTTP API.

### Технологический стек

Проект использует следующие технологии:
- **Python 3.13** — основной язык программирования
- **FastAPI** — асинхронный веб-фреймворк для создания API
- **Uvicorn** — ASGI-сервер для запуска приложений
- **HTTPX** — асинхронный HTTP-клиент для межсервисного взаимодействия
- **Docker** — контейнеризация сервисов
- **Poetry** — управление зависимостями и сборка

## Описание сервисов

### 1. Сервис продуктов (Product Service)

Сервис отвечает за хранение и выдачу информации о товарах.

**Модель продукта:**
```python
{
    "id": "pencil",
    "name": "Pencil",
    "price": 1.50,
    "available": true
}
```

### 2. Сервис скидок (Discount Service)

Реализует бизнес-правила для расчета скидок.


**Правила расчета (в порядке приоритета):**

| Приоритет | Условие | Скидка | Пояснение |
|-----------|---------|--------|-----------|
| 1 | `STUDENT10` промокод | 10% | Студенческая скидка |
| 2 | `PROMO20` промокод | 20% | Маркетинговая акция |
| 3 | Количество ≥ 10 | 15% | Оптовая скидка крупного объема |
| 4 | Количество ≥ 5 | 5% | Оптовая скидка |
| 5 | Цена товара > 100 | 3% | Премиальный товар |
| - | Иначе | 0% | Скидка не применяется |

### 3. Сервис заказов (Order Service)

Центральный компонент, который:
1. Получает запрос на создание заказа
2. Запрашивает информацию о товаре из Product Service
3. Запрашивает расчет скидки из Discount Service
4. Вычисляет финальную стоимость заказа
5. Возвращает клиенту детализированный ответ

**Пример запроса:**
```json
POST /orders
{
    "product_id": "notebook",
    "quantity": 15,
    "promo_code": "STUDENT10"
}
```

**Пример ответа:**
```json
{
    "product_id": "notebook",
    "quantity": 15,
    "unit_price": 4.20,
    "subtotal": 63.00,
    "discount_percent": 15.0,
    "discount_reason": "Wholesale discount for ordering 10+ items",
    "discount_amount": 9.45,
    "total": 53.55
}
```

## Особенности реализации

### Сетевая изоляция

Все сервисы запущены в кастомной Docker-сети `service-net` с подсетью `172.28.10.0/24`.

### Конфигурация через переменные окружения

Сервис заказов использует переменные окружения для определения адресов зависимостей:

```python
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://127.0.0.1:8001")
DISCOUNT_SERVICE_URL = os.getenv("DISCOUNT_SERVICE_URL", "http://127.0.0.1:8003")
```

## Docker-контейнеризация

### Структура образов

Каждый сервис использует многоступенчатую сборку с базовым образом `python:3.13-slim`.

Пример Dockerfile:
```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --only main --no-root
COPY src/app ./app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

Файл `docker-compose.yaml` описывает все три сервиса и их связи:

```yaml
services:
  product-service:
    build: ./product_service
    ports: ["8001:8000"]
    networks: [service-net]

  discount-service:
    build: ./discount_service
    ports: ["8003:8000"]
    networks: [service-net]

  order-service:
    build: ./order_service
    ports: ["8002:8000"]
    environment:
      PRODUCT_SERVICE_URL: http://product-service:8000
    depends_on: [product-service, discount-service]
    networks: [service-net]
```

Запуск всех сервисов одной командой:
```bash
docker-compose up -d
```

## Управление зависимостями

Для каждого сервиса зависимости управляются отдельно через Poetry. 

Пример `pyproject.toml` (единый для всех сервисов, но с разной структурой каталогов):
```toml
[project]
name = "discount-service"
version = "0.0.1"
requires-python = ">=3.13"
dependencies = [
    "uvicorn[standard] (>=0.46.0,<0.47.0)",
    "fastapi (>=0.136.1,<0.137.0)",
    "httpx (>=0.28.1,<0.29.0)",
]
```

### Логирование ошибок

При недоступности внешних сервисов возвращаются соответствующие HTTP-статусы:
- `503 Service Unavailable` — при проблемах с сетью
- `502 Bad Gateway` — при некорректных ответах от зависимых сервисов
- `422 Unprocessable Entity` — семантическая ошибка в запросе
- `404 Not Found` — при отсутствии товара

## Запуск проекта

### Локальная разработка

```bash
# В терминале 1 - Product Service
cd product_service
poetry install
poetry run uvicorn app.main:app --port 8001

# В терминале 2 - Discount Service  
cd discount_service
poetry install
poetry run uvicorn app.main:app --port 8003

# В терминале 3 - Order Service
cd order_service
poetry install
POETRY_RUN poetry run uvicorn app.main:app --port 8002
```

### Запуск в Docker

```bash
docker-compose up --build
```
---

**Исходный код:** доступен в репозитории проекта  
**Авторы:** Илья Горохов и Сергей Плескунов
**Лицензия:** MIT