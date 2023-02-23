from django.db import models

# Create your models here.
class employer(models.Model):
    name = models.CharField(max_length=255)
    language= models.CharField(max_length=255)
    phone = models.BigIntegerField()
    rating = models.FloatField()
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name