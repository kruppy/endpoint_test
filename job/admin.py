from django.contrib import admin
from .models.job import Job
from .models.schedule import Schedule
from .models.topic import Topic

admin.site.register(Job)
admin.site.register(Schedule)
admin.site.register(Topic)
