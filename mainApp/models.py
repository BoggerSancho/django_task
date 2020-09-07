from django.db import models


class URL_table(models.Model):
    user_id = models.IntegerField()
    url = models.CharField(max_length=200)
