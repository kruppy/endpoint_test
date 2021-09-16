from django.db import models
from .job import Job


COLOR_CHOICES = (
    ("bg-green-300", "Green"),
    ("bg-red-300", "Red"),
    ("bg-yellow-300", "Yellow"),
    ("bg-blue-300", "Blue"),
    ("bg-indigo-300", "Indigo"),
    ("bg-purple-300", "Purple"),
    ("bg-pink-300", "Pink"),
    ("bg-teal-300", "Teal"),
    ("bg-gray-300", "Gray"),

)

class Schedule(models.Model):
    title = models.CharField(max_length=255)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    start = models.TimeField()
    end = models.TimeField()
    field_color = models.CharField(max_length=25, choices=COLOR_CHOICES, default="bg-gray-300")

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    @property
    def border_color(self):
        return self.field_color.replace("300", "800")

    @property
    def text_color(self):
        return self.border_color.replace("bg", "text")

    def __str__(self):
        return self.title