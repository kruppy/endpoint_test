from rest_framework import serializers
from ..models.contact import Contact
from .company_serializer import CompanySerializer

class ContactSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False)
    class Meta:
        model = Contact
        fields = '__all__'