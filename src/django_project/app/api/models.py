from django.db import models


class Tutor(models.Model):
    class Meta:
        db_table = "tutor"

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
