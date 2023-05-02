from django.db import models
from users.models import users
from category.models import category

# Create your models here.
status_choices = (('Hiring', 'Hiring'), ('In Progress',
                  'In Progress'), ('Done', 'Done'), ('Payment', 'Payment'), ('Complete', 'Complete'))

class job(models.Model):
   title = models.CharField(max_length=255)
   description= models.TextField()
   pay = models.PositiveIntegerField()
   required_skills = models.TextField()
   status = models.CharField(max_length=255, choices=status_choices)
   employer = models.ForeignKey(users, on_delete=models.CASCADE, related_name='employer', null=True)
   service_provider = models.ForeignKey(users, to_field="email", related_name='service_provider', null=True, blank=True, on_delete=models.CASCADE)
   category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return str({field.name: getattr(self, field.name) for field in self._meta.fields})

