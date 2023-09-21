from django.contrib import admin

from .base_admin import AutoConfigAdmin
from ..app_forms import FileForm
from ..app_models import File


@admin.register(File)
class FileAdmin(AutoConfigAdmin):
    form = FileForm
