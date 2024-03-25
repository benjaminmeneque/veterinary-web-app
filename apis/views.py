from rest_framework import mixins, viewsets

from apis import serializers
from booking import models


# Create your views here.
class DoctorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class VeterinaryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Veterinary.objects.all()
    serializer_class = serializers.VeterinarySerializer


class PetViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer


class VeterinaryInstanceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.VeterinaryInstance.objects.all()
    serializer_class = serializers.VeterinaryInstanceSerializer


class SpecialtiesViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Specialties.objects.all()
    serializer_class = serializers.SpecialtiesSerializer


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
