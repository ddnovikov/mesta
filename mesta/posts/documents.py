from django_elasticsearch_dsl import DocType, Index, fields

from .models import Post

posts = Index('posts')


@posts.doc_type
class PostDocument(DocType):
    tags = fields.StringField(attr="tags_as_string")

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content'
        ]

    def __repr__(self):
        return f'PostDocument(title={self.title}, ' \
               f'tags={self.tags})'
