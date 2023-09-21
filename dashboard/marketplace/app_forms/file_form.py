from .base_forms import ChoicesModelForm
from ..app_models import File, ConstantsFile


class FileForm(ChoicesModelForm):
    class Meta:
        model = File
        fields = ConstantsFile.get_fields()
