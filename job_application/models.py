from django.db import models
from service_provider.models import service_provider
from job.models import job

class job_application(models.Model):
    service_provider_id = models.ForeignKey(service_provider, on_delete=models.CASCADE)
    job_id = models.ForeignKey(job, on_delete=models.CASCADE)

# Create your models here.
