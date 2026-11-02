# Little Lemon — restaurant API

Django REST API for a restaurant (the Meta Back-End Developer capstone):
menu items, table bookings, and token authentication, plus a static home
page.

## Stack

- Python 3.11, Django 5.2, Django REST Framework
- Djoser + DRF token authentication
- MySQL (via mysqlclient)

## Endpoints

| Method | Path | Auth | Purpose |
|---|---|---|---|
| GET | `/restaurant/` | | Static home page |
| GET, POST | `/restaurant/api/menu-items/` | POST needs a token | List / add menu items |
| GET, PUT, PATCH, DELETE | `/restaurant/api/menu-items/<id>/` | writes need a token | One menu item |
| GET, POST, PUT, DELETE | `/restaurant/booking/tables/` | token | Table bookings (DRF router) |
| POST | `/auth/users/` | | Register (Djoser) |
| POST | `/auth/token/login/`, `/obtain-token/` | | Get an auth token |
| GET | `/restaurant/api/msg` | token | Check that authentication works |

Send the token as `Authorization: Token <token>`.

## Running locally

The project is in `Capstone_project/littlelemonFinal/`. Requires a local
MySQL server. Connection settings come from environment variables:
`DB_NAME` (default `my_database`), `DB_USER` (default `root`), `DB_PASSWORD`,
`DB_HOST` (default `127.0.0.1`), `DB_PORT` (default `3306`).

```sh
python -m venv venv
venv\Scripts\activate          # Windows; on macOS/Linux: source venv/bin/activate
pip install django==5.2.9 djangorestframework==3.16.1 djoser==2.3.3 mysqlclient==2.2.7
cd Capstone_project/littlelemonFinal
python manage.py migrate
python manage.py runserver
```

## Tests

```sh
cd Capstone_project/littlelemonFinal
python manage.py test tests
```

2 tests (`tests/test_views.py`), covering the menu model and the menu list view.
