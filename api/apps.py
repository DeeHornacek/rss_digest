from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the 'api' application.
    Defines the default primary key field type and app name.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
