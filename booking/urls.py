from django.urls import path

from booking import views

urlpatterns = [
    # create views
    path(
        "booking/",
        views.VeterinaryInstanceCreate.as_view(),
        name="veterinary-instance-create",
    ),
    path("register/doctor/", views.DoctorCreate.as_view(), name="doctor-create"),
    path(
        "register/veterinary/",
        views.VeterinaryCreate.as_view(),
        name="veterinary-create",
    ),
    path("register/pet/", views.PetCreate.as_view(), name="pet-create"),
    path(
        "register/specialties/",
        views.SpecialtiesCreate.as_view(),
        name="specialties-create",
    ),
    # update views
    path(
        "booking/<uuid:pk>/update/",
        views.VeterinaryInstanceUpdate.as_view(),
        name="veterinary-instance-update",
    ),
    path("update/doctor/<int:pk>/", views.DoctorUpdate.as_view(), name="doctor-update"),
    path(
        "update/veterinary/<int:pk>/",
        views.VeterinaryUpdate.as_view(),
        name="veterinary-update",
    ),
    path("update/pet/<int:pk>/", views.PetUpdate.as_view(), name="pet-update"),
]
