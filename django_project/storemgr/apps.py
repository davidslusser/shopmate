from django.apps import AppConfig


class StoremgrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "storemgr"

    def ready(self):
        import storemgr.signals
