from .base_forms import ChoicesModelForm
from ..app_models import Review, ConstantsReview


class ReviewForm(ChoicesModelForm):
    class Meta:
        model = Review
        fields = ConstantsReview.get_fields()
