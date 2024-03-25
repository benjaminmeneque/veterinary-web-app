from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.SimpleRouter()
router.register(r"doctors", views.DoctorViewSet)
router.register(r"pets", views.PetViewSet)
router.register(r"veterinarians", views.VeterinaryViewSet)
router.register(r"veterinarian-instances", views.VeterinaryInstanceViewSet)
router.register(r"specialties", views.SpecialtiesViewSet)
router.register(r"services", views.ServiceViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
