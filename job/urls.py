# URLs file of app 'job'
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.job_viewset import JobViewSet
from .views.schedule_viewset import ScheduleViewSet
from .views.topic_viewset import TopicViewSet

router = DefaultRouter()
router.register("jobs", JobViewSet)
router.register("schedule", ScheduleViewSet)
router.register("topic", TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]