import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Specialties(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("specialties-detail", args=[str(self.id)])


class Service(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Veterinary(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    contact_number = PhoneNumberField(blank=False, null=False)
    services = models.ManyToManyField(Service)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.address})"

    def get_absolute_url(self):
        return reverse("veterinary-detail", args=[str(self.id)])


class Doctor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    clinic = models.ForeignKey(Veterinary, on_delete=models.CASCADE)
    specialties = models.ManyToManyField(Specialties)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.last_name},{self.first_name}"

    def get_absolute_url(self):
        return reverse("doctor-detail", args=[str(self.id)])


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    date_birth = models.DateField()
    breed = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pet-detail", args=[str(self.id)])


class VeterinaryInstance(models.Model):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    APPOINTMENT_STATUS = {
        PENDING: "Pending",
        APPROVED: "Approved",
        DECLINED: "Declined",
    }
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    veterinary_name = models.ForeignKey(Veterinary, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.ForeignKey(Pet, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=APPOINTMENT_STATUS, default="Pending"
    )

    class Meta:
        ordering = ["create_date"]

    def __str__(self):
        return f"{self.veterinary_name}"

    def get_absolute_url(self):
        return reverse("veterinary-instance-detail", args=[str(self.id)])
