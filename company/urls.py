# URLs file of app 'company'
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.company_viewset import CompanyViewSet
from .views.benefit_viewset import BenefitsViewSet
from .views.contact_viewset import ContactViewSet, CompanyContactsListView
from .views.jobpost_viewset import JobpostViewset

router = DefaultRouter()
router.register("companys", CompanyViewSet)
router.register("benefits", BenefitsViewSet)
router.register("contacts", ContactViewSet)
router.register("jobpost", JobpostViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('contacts/<uuid:id>/', CompanyContactsListView.as_view(), name='contacts'),
]
