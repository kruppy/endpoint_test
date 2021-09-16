from django.db import models
import uuid


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    company_name = models.CharField(max_length=55)
    img_url = models.URLField(max_length=400)
    backgroundimg_url = models.URLField(max_length=400)
    website_url = models.URLField(max_length=400)
    linkedin_url = models.URLField(max_length=400)
    location = models.CharField(max_length=55)
    #sector = models.ManyToManyField(to=Sector, blank=True)
    about = models.TextField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"

    def __str__(self):
        return self.company_name
