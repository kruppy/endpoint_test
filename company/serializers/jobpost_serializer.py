from rest_framework import serializers
from ..models.jobpost import Jobpost


class JobpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobpost
        fields = '__all__'
