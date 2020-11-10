from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):  # ref according to django documentation.
        import users.signals
