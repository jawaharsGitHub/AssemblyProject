from django.db import models


class CropIns(models.Model):
    total_parappu = models.CharField(max_length=30)
    total_cent = models.CharField(max_length=30)
    total_amount = models.CharField(max_length=30)

