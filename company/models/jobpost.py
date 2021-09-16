from django.db import models
import uuid
from .company import Company

TYPE_CHOICES = (
    ("Trainee", "Trainee"),
    ("Duales Studium", "Duales Studium"),
    ("Praktikum", "Praktikum"),
    ("Werkstudent", "Werkstudent"),
    ("Vollzeit", "Vollzeit"),
    ("Teilzeit", "Teilzeit")
)


class Jobpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=75)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    external_link = models.URLField(max_length=400)
    location = models.CharField(max_length=45)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default="Vollzeit")
    position_overview = models.TextField()
    qualifications = models.TextField()
    compensation = models.TextField()

    def __str__(self):
        return self.title
        