from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import setup_groups
        post_migrate.connect(setup_groups, sender=self)

