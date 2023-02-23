from django.db import models

# Create your models here.
class category(models.Model):
   job_category= models.CharField(max_length=255)
   icon_url= models.TextField()

   def __str__(self) -> str:
    return self.job_category