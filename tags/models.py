from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Generic Relationship using ContentType
    # type (product, video, article) to select type of table/object
    # ID (to traverse in table rows)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
