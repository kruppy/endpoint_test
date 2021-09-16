from django.contrib import admin
from .models.company import Company
from .models.benefit import Benefits
from .models.contact import Contact


class BenefitsAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


admin.site.register(Company)
admin.site.register(Benefits, BenefitsAdmin)
admin.site.register(Contact)
