import os
import sys

from django.apps import AppConfig

current_dir = os.getcwd()
if current_dir not in sys.path:
    sys.path.append(current_dir)


class AdminConfig(AppConfig):
    from utils.django_configure import get_django_name
    default_auto_field = 'django.db.models.BigAutoField'
    name = get_django_name()
