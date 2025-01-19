myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    todo/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        migrations/
            __init__.py


find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

