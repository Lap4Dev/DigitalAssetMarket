from django.contrib import admin

from .base_admin import AutoConfigAdmin
from ..app_forms import ReviewForm
from ..app_models import Review


@admin.register(Review)
class ReviewAdmin(AutoConfigAdmin):
    form = ReviewForm
