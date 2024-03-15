from rest_framework import serializers

from booking import models


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
    status = serializers.SerializerMethodField()

    class Meta:
        model = models.VeterinaryInstance
        fields = [
            "id",
            "veterinary_name",
            "doctor_name",
            "owner",
            "pet_name",
            "description",
            "create_date",
            "status",
        ]

    def get_status(self, obj):
        return dict(models.VeterinaryInstance.BOOKING_STATUS).get(obj.status)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["owner"] = instance.owner.username
        data["doctor_name"] = (
            instance.doctor_name.first_name + " " + instance.doctor_name.last_name
        )
        data["pet_name"] = instance.pet_name.name
        data["veterinary_name"] = instance.veterinary_name.name
        return data
