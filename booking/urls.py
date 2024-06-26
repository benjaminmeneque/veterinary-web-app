from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from booking import views

urlpatterns = [
    # create
    path(
        "bookings/new/",
        views.VeterinaryInstanceCreate.as_view(),
        name="veterinary-instance-create",
    ),
    path("doctors/new/", views.DoctorCreate.as_view(), name="doctor-create"),
    path(
        "veterinarians/new/",
        views.VeterinaryCreate.as_view(),
        name="veterinary-create",
    ),
    path("pets/new/", views.PetCreate.as_view(), name="pet-create"),
    path(
        "specialties/new/",
        views.SpecialtiesCreate.as_view(),
        name="specialties-create",
    ),
    path("services/new/", views.CreateService.as_view(), name="service-create"),
    # update
    path(
        "bookings/<uuid:pk>/update/",
        views.VeterinaryInstanceUpdate.as_view(),
        name="veterinary-instance-update",
    ),
    path(
        "doctors/<int:pk>/update/", views.DoctorUpdate.as_view(), name="doctor-update"
    ),
    path(
        "veterinarians/<int:pk>/update/",
        views.VeterinaryUpdate.as_view(),
        name="veterinary-update",
    ),
    path("pets/<int:pk>/update/", views.PetUpdate.as_view(), name="pet-update"),
    # detail
    path("doctors/<int:pk>/", views.DoctorDetail.as_view(), name="doctor-detail"),
    path(
        "veterinarians/<int:pk>/",
        views.VeterinaryDetail.as_view(),
        name="veterinary-detail",
    ),
    path(
        "bookings/<uuid:pk>/",
        views.VeterinaryInstanceDetail.as_view(),
        name="veterinary-instance-detail",
    ),
    path("pets/<int:pk>/", views.PetDetail.as_view(), name="pet-detail"),
    # list
    path(
        "bookings/",
        views.VeterinaryInstanceList.as_view(),
        name="veterinary-instance-list",
    ),
    path("pets/", views.PetList.as_view(), name="pet-list"),
    path("veterinarians/", views.VeterinaryList.as_view(), name="veterinarians-list"),
    path("doctors/", views.DoctorList.as_view(), name="doctor-list"),
    path("", views.index, name="home"),
    path("search/", views.SearchResultsList.as_view(), name="search-results"),
    path("appointments/", views.ApppoinmentsView, name="appointment"),
    # delete
    path("pet/delete/<int:pk>/", views.PetDelete.as_view(), name="pet-delete"),
    path(
        "booking/delete/<uuid:pk>/",
        views.VeterinaryInstanceDelete.as_view(),
        name="veterinary-instance-delete",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
