from django.utils import timezone

from django.db import models


class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class CustomDefaultManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    objects = CustomDefaultManager()
    all_objects = AllManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()
