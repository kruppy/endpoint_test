from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name
