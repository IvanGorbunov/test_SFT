from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateModelMixin(models.Model):
    created_at = models.DateTimeField(_('Date of creation'), auto_now_add=True)

    class Meta:
        abstract = True


class DeleteModelMixin(models.Model):

    is_delete = models.BooleanField(_('Deleted'), default=False)

    class Meta:
        abstract = True

    def destroy(self):
        self.is_delete = True
        self.save(update_fields=('is_delete',))
