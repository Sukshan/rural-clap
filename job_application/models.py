from django.db import models
from users.models import users
from job.models import job

class job_application(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    job_id = models.ForeignKey(job, on_delete=models.CASCADE)

# Create your models here.
