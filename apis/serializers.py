from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
