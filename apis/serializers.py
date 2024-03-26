from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from booking import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(UserSerializer, self).create(validated_data)


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = [
            "id",
            "first_name",
            "last_name",
            "specialties",
            "email",
            "phone_number",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["specialties"] = [
            specialties.name for specialties in instance.specialties.all()
        ]
        return data


class VeterinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Veterinary
        fields = [
            "id",
            "name",
            "address",
            "contact_number",
        ]


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pet
        fields = [
            "id",
            "owner",
            "name",
            "date_birth",
            "breed",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["owner"] = instance.owner.username
        return data


class VeterinaryInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VeterinaryInstance
        fields = [
            "id",
            "veterinary_name",
            "doctor",
            "owner",
            "pet_name",
            "description",
            "create_date",
            "status",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["owner"] = instance.owner.username
        data["pet_name"] = instance.pet_name.name
        data["veterinary_name"] = instance.veterinary_name.name
        if instance.doctor != None:
            data["doctor"] = (
                instance.doctor.first_name + " " + instance.doctor.last_name
            )
        return data


class SpecialtiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialties
        fields = ["name"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ["name"]
