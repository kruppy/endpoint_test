from rest_framework import viewsets
from ..models.jobpost import Jobpost
from ..serializers.jobpost_serializer import JobpostSerializer


class JobpostViewset(viewsets.ModelViewSet):
    queryset = Jobpost.objects.all()
    serializer_class = JobpostSerializer
