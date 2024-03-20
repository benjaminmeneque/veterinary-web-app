from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets

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


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
