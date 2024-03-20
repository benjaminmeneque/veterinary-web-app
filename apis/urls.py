from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.SimpleRouter()
router.register(r"doctors", views.DoctorViewSet)
router.register(r"pets", views.PetViewSet)
router.register(r"veterinarians", views.VeterinaryViewSet)
router.register(r"veterinarian-instances", views.VeterinaryInstanceViewSet)


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path("", include(router.urls)),
]
