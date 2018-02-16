from places.models import FoodService
from places.forms import PlaceForm


class FoodServiceForm(PlaceForm):
    class Meta(PlaceForm.Meta):
        model = FoodService
        fields = super(FoodServiceForm.fields).fields + [
            'place_type',
            'menu',
            'parking',
            'bank_cards',
            'wi_fi',
            'banquets',
            'delivery',
            'catering'
        ]
