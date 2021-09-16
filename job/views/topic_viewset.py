from rest_framework import viewsets
from ..models.topic import Topic
from ..serializers.topic_serializer import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
