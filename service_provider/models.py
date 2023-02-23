from django.db import models

# Create your models here.
class service_provider(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()
    phone = models.BigIntegerField()
    rating =models.FloatField()
    location = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    expected_payment = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=255)
    language= models.CharField(max_length=255)
    phone = models.BigIntegerField()
    rating = models.FloatField()
    location = models.CharField()
    gender = models.CharField()

    def __str__(self) -> str:
        return self.name

class  category(models.Model):
    job_category= models.CharField(max_length=255)
    icon_url= models.TextField()


#main table
class job(models.Model):
    title = models.CharField()
    description= models.TextField()
    #employer_id