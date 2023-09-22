import uuid

from django.core.validators import MinValueValidator
from django.db import models

from . import TelegramUser
from ._constants import ConstantsFile, StatusState


class File(models.Model):
    file_id = models.CharField(
        verbose_name=ConstantsFile.file_id,
        max_length=10,
        default=str(uuid.uuid4().hex[:10]), primary_key=True
    )
    owner_user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name=ConstantsFile.owner_user
    )
    file_name = models.CharField(verbose_name=ConstantsFile.file_name, max_length=45)
    file_description = models.TextField(verbose_name=ConstantsFile.file_description)
    file_dir = models.CharField(verbose_name=ConstantsFile.file_dir, max_length=255)
    file_price = models.DecimalField(
        verbose_name=ConstantsFile.file_price,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    file_pub_date = models.DateField(verbose_name=ConstantsFile.file_pub_date)

    file_status = models.CharField(
        verbose_name=ConstantsFile.file_status,
        choices=StatusState.get_choices(),
        max_length=StatusState.get_choice_max_length()
    )

    def __str__(self):
        return f'File: {self.file_name} of {self.owner_user}'

    class Meta:
        verbose_name = ConstantsFile.Meta.verbose_name
        verbose_name_plural = ConstantsFile.Meta.verbose_name_plural
