from django.db import models
from .company import Company

class Contact(models.Model):
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=55)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.firstname + " " + self.lastname

