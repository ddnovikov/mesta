from django_elasticsearch_dsl import DocType, Index, fields
from places.models import Place

places = Index('places')


@places.doc_type
class PlaceDocument(DocType):
    tags = fields.StringField(attr="tags_to_string")
    subway = fields.StringField(attr="subway_to_string")

    class Meta:
        model = Place
        fields = [
            'name',
            'slug',
            'description',
            'country',
            'region',
            'city',
            'street',
            'site',
        ]

    def __repr__(self):
        return f'PlaceDocument(name={self.name}, tags={self.tags}, city={self.city})'
