# bookstore
Minimal "bookstore" app with Django and DRF


## First time setup
```
poetry install --with=app
```


## Run development server

1. Start database for local development.
```bash
docker compose -f project/docker-compose.yml up -d
```

2. Generate migrations
```
python manage.py makemigrations
```

3. Apply migrations
```
python manage.py migrate
```

4. Run server
```
python manage.py runserver
```

5. Django shell
```
python manage.py shell
```
