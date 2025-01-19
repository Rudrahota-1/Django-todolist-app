from django.apps import AppConfig

class TodoappConfig(AppConfig):  # Class name matches the app name in CamelCase
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'  # App name matches the folder name
