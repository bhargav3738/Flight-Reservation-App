from django.apps import AppConfig


# class FlightsConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "flights"
# from django.apps import AppConfig


class FlightsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flights"
    def ready(self):
        import flights.signals