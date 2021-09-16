from rest_framework import serializers
from ..models.benefit import Benefits

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = '__all__'