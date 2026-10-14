# BAS-IP API — актуальная версия

HTTP API оборудования BAS-IP: **только текущие (current) версии** по каждому семейству.
Источник — спецификации OpenAPI, опубликованные на `developers.bas-ip.com`.

## Состав

| Семейство устройств | Операций |
|---|---|
| android-panels | 230 |
| ingenic-mips-panels | 142 |
| camdroid-panels | 145 |
| door-controller | 78 |
| android-monitors | 77 |
| camdroid-monitors | 66 |
| camdroid-lift-controller | 33 |
| **Итого** | **771** |

## Файлы

```
.
├── README.md              # этот файл
├── METHODS.md             # плоская таблица: метод | путь | название | теги
├── openapi/               # 7 спецификаций OpenAPI 3.0.0 (по одной на семейство)
│   ├── android-panels__current.json
│   ├── android-monitors__current.json
│   ├── camdroid-panels__current.json
│   ├── camdroid-monitors__current.json
│   ├── camdroid-lift-controller__current.json
│   ├── door-controller__current.json
│   └── ingenic-mips-panels__current.json
├── docs/
│   └── bas-ip-api.md      # полный человекочитаемый справочник (русский)
└── gen.py                 # генератор METHODS.md и docs/bas-ip-api.md
```

## Быстрый старт

- **Импорт в Postman/Swagger UI:** возьмите `openapi/<device>__current.json`.
- **Человекочитаемый вид:** откройте `docs/bas-ip-api.md`.
- **Найти эндпоинт:** `METHODS.md`.

## Серверы и авторизация

- **Локальная сеть устройства:** `http://<IP-панели>/api/v1` (у разных семейств
  префикс отличается — `/api`, `/api/v0`, `/api/v1`; точный указан в спецификации).
- **Mock SwaggerHub:** `https://virtserver.swaggerhub.com/basip/<api-name>/<version>` —
  для тестов без железа.
- **Авторизация:** HTTP Bearer (`Authorization: Bearer <token>`); логин через
  соответствующий эндпоинт раздела `auth`.

## Регенерация

```bash
python3 gen.py     # пересобирает METHODS.md и docs/bas-ip-api.md из openapi/
```
