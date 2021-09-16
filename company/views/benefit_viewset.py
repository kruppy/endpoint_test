from rest_framework import viewsets, generics
from ..models.benefit import Benefits
from ..serializers.benefit_serializer import BenefitSerializer


"""
class BenefitReadView(generics.ListAPIView):
    serializer_class = BenefitSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        company = self.kwargs['company']
        queryset = self.model.objects.filter(company=company)
        return queryset
"""


class BenefitsViewSet(viewsets.ModelViewSet):
    queryset = Benefits.objects.all()
    serializer_class = BenefitSerializer