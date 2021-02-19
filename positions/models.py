from django.db import models

from irantalent.abstract_models import AbstractBaseModel


class PositionLocation(AbstractBaseModel):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    address_detail = models.TextField(null=True)

    @property
    def full_address(self):
        return f"{self.country}, {self.city}, {self.address_detail}"


class PositionCategory(AbstractBaseModel):
    category = models.CharField(max_length=100)
    detail = models.TextField()


class Position(AbstractBaseModel):
    title = models.TextField()
    category = models.ForeignKey(
        'PositionCategory',
        on_delete=models.DO_NOTHING,
        related_name='positions',
        related_query_name='position'
    )
    min_age = models.IntegerField(null=True)
    max_age = models.IntegerField(null=True)
    education = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, null=True)
    salary = models.BigIntegerField(null=True)
    location = models.ForeignKey(
        'PositionLocation',
        on_delete=models.SET_NULL,
        null=True,
        related_name='positions',
        related_query_name='position'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()
    lived_at = models.DateTimeField()
