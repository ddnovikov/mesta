from ..models import FoodService
from ..forms import PlaceForm


class FoodServiceForm(PlaceForm):
    class Meta(PlaceForm.Meta):
        model = FoodService
        fields = PlaceForm.Meta.fields + [
            'place_type',
            'menu',
            'parking',
            'bank_cards',
            'wi_fi',
            'banquets',
            'delivery',
            'catering'
        ]
