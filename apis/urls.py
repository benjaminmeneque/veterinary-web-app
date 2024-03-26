from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.SimpleRouter()
router.register(r"doctors", views.DoctorViewSet)
router.register(r"pets", views.PetViewSet)
router.register(r"clinics", views.VeterinaryViewSet)
router.register(r"clinics-instance", views.VeterinaryInstanceViewSet)
router.register(r"specialties", views.SpecialtiesViewSet)
router.register(r"services", views.ServiceViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
