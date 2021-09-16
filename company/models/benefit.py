from django.db import models
from .company import Company
import uuid

class Benefits(models.Model):
    name = models.CharField(max_length=35)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    icon = models.CharField(max_length=35)

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

    def __str__(self):
        return self.name






