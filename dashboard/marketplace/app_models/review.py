from django.db import models

from . import File
from ._constants import ConstantsReview
from ..app_models import TelegramUser


class Review(models.Model):

    review_id = models.AutoField(verbose_name=ConstantsReview.review_id, primary_key=True)
    review_message = models.TextField(verbose_name=ConstantsReview.review_message)
    review_rate = models.IntegerField(
        verbose_name=ConstantsReview.review_rate,
        default=1,
        choices=[(i, i) for i in range(1, 6)]
    )
    review_date = models.DateTimeField(verbose_name=ConstantsReview.review_date, auto_now_add=True)
    owner_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name=ConstantsReview.owner_user)
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name=ConstantsReview.file)

    def __str__(self):
        return f'Review #{self.review_id} to {self.file}'

    class Meta:
        verbose_name = ConstantsReview.Meta.verbose_name
        verbose_name_plural = ConstantsReview.Meta.verbose_name_plural
