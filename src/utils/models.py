
from django.db import models


class CreateModelMixin(models.Model):
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        abstract = True

