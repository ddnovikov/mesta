from django_elasticsearch_dsl import DocType, Index, fields
from places.models import Place, FoodService

places = Index('places')
food_services = Index('food_services')


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


'''
    A few thoughts on DocType models for future work with 
    django-elasticsearch-dsl (DED).
    
    Actually it seems like it would be better to inherit FoodServiceDocument 
    from PlaceDocument, but for now i'll leave it like this, 
    because DED's structure does not support normal django-style
    model inheritance (and class Meta inheritance too) like Django does.
     
    About class Meta. On one hand, its behaviour is really OK: Django works the same in this
    case - Meta can be inherited only from abstract base classes. 
    But on the other hand, Meta in Django and in DED are very
    different, and it may be very useful to make Meta inheritable.
    
    Also, I found out that class Meta inheritance can be fixed really
    easy with just assigning Meta property to appropriate class (DED's DocTypeMeta,
    defined in documents.py). But the huge problem here is, that implementation of
    Django-like behaviour in models is quite hard task.
'''


@food_services.doc_type
class FoodServiceDocument(DocType):
    tags = fields.StringField(attr="tags_to_string")
    subway = fields.StringField(attr="subway_to_string")

    class Meta:
        model = FoodService
        fields = [
            'name',
            'slug',
            'description',
            'country',
            'region',
            'city',
            'street',
            'site',
            'parking',
            'bank_cards',
            'wi_fi',
            'banquets',
            'delivery',
            'catering'
        ]

    def __repr__(self):
        return f'FoodServiceDocument(name={self.name}, tags={self.tags}, city={self.city})'
