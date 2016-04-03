from django.db import models


class OneModel(models.Model):

    a_charfield = models.CharField(max_length=255, null=True, blank=True)
    a_date = models.DateTimeField(null=True, blank=True)
    other_date = models.DateTimeField(null=True, blank=True)


class AnotherModel(models.Model):

    a_big_int = models.BigIntegerField(default=0, blank=False)
    a_model = models.ForeignKey("OneModel", null=True, blank=True)
