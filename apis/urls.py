from django.urls import include, path
from rest_framework import routers

from apis import views

router = routers.SimpleRouter()
router.register(r"doctors", views.DoctorViewSet)
router.register(r"pets", views.PetViewSet)
router.register(r"veterinarians", views.VeterinaryViewSet)
router.register(r"veterinarian-instances", views.VeterinaryInstanceViewSet)


urlpatterns = [
    path("dj-rest-auth/facebook/", views.FacebookLogin.as_view(), name="fb_login"),
    path("dj-rest-auth/google/", views.GoogleLogin.as_view(), name="google_login"),
    path("", include(router.urls)),
]
