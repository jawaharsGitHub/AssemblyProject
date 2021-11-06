from django.db import models


class CropInsModel(models.Model):
    parappu_list = models.TextField(max_length=30)
    acre_amount = models.CharField(max_length=30)
    total_cent = models.CharField(max_length=30)
    total_acre = models.CharField(max_length=30)
    total_amount = models.CharField(max_length=30)
    round_amount = models.CharField(max_length=30)
    total_parappu = models.CharField(max_length=30)
    device_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.device_name}-{self.total_parappu}-{self.round_amount}"