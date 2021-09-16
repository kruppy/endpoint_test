from rest_framework import viewsets, generics
import uuid
from ..models.contact import Contact
from ..serializers.contact_serializer import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CompanyContactsListView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        company_uuid = self.kwargs['company']
        return Contact.objects.filter(company__uuid=company_uuid)


# django.db.models.fields.related.ForeignKey: company

# django.db.models.fields.UUIDField: id