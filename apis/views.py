from rest_framework import viewsets

from apis import serializers
from booking import models


# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class VeterinaryViewSet(viewsets.ModelViewSet):
    queryset = models.Veterinary.objects.all()
    serializer_class = serializers.VeterinarySerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer


class VeterinaryInstanceViewSet(viewsets.ModelViewSet):
    queryset = models.VeterinaryInstance.objects.all()
    serializer_class = serializers.VeterinaryInstanceSerializer
