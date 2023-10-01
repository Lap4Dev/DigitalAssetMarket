config_name = 'marketplace'


def set_django_conf_name(name):
    global config_name
    config_name = name


def get_django_name():
    global config_name
    return config_name


def configure_django():
    import os
    import django
    set_django_conf_name('dashboard.marketplace')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.dashboard.settings")
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()


