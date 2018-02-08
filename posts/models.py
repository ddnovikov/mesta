# from django.conf import settings
#
# from django.db import models
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=120)
#     slug = models.SlugField(unique=True)
#     content = models.TextField()
#     image = models.ImageField(upload_to=upload_location,
#                               null=True,
#                               blank=True,
#                               height_field='height_field',
#                               width_field='width_field')
#     height_field = models.IntegerField(default=0)
#     width_field = models.IntegerField(default=0)
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     draft = models.BooleanField(default=False)
#
#     publish = models.DateField(auto_now=False, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     objects = PostManager()
#
#     def __repr__(self):
#         return f'Post(title={self.title}, timestamp={self.timestamp})'
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('posts:detail', kwargs={'slug': self.slug})
#
#     def get_markdown(self):
#         return mark_safe(markdown(self.content))
#
#     @property
#     def comments(self):
#         return Comment.objects.filter_by_instance(self)
#
#     @property
#     def get_content_type(self):
#         return ContentType.objects.get_for_model(self.__class__)
#
#     class Meta:
#         ordering = ["-timestamp", "-updated"]
#
