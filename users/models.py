from django.db import models

class users(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True,)
    location = models.CharField(max_length=255, null=True, blank= True)
    phone = models.BigIntegerField(null=True, blank= True)
    rating = models.FloatField(null=True, blank= True)
    gender = models.CharField(max_length=255, null=True, blank= True)
    email = models.EmailField(max_length=254, null= True, blank= True, unique=True)
    isEmployer = models.BooleanField(null= True, blank= True)
    description = models.TextField(null=True, blank=True)
    skills = models.TextField(blank= True, null= True)
    expectedPayment =  models.PositiveIntegerField(blank= True, null= True)
    category = models.TextField(null=True,blank=True) # job  category
    modelRating= models.FloatField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    education = models.TextField(null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)
    created_jobs = models.TextField(null=True, blank= True)
    applied_jobs= models.TextField(null=True, blank= True)

   
    def __str__(self):
        return str({field.name: getattr(self, field.name) for field in self._meta.fields})
