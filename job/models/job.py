from django.db import models
import uuid
from django.utils import timezone

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    job_title = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    publication_date = models.DateTimeField(default=timezone.now())
    img_url = models.URLField(max_length=400)
    description = models.TextField(default="please add a description")
    about = models.TextField(default="please add an about section")

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.job_title