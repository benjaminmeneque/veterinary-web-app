import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class Specialties(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("specialties-detail", args=[str(self.id)])


class Doctor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    specialties = models.ManyToManyField(Specialties)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.last_name + "," + self.first_name

    def get_absolute_url(self):
        return reverse("doctor-detail", args=[str(self.id)])


class Veterinary(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    contact_number = PhoneNumberField(blank=False, null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("veterinary-detail", args=[str(self.id)])


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
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
    BOOKING_STATUS = (
        ("p", "pending"),
        ("a", "approved"),
        ("d", "declined"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    veterinary_name = models.ForeignKey(Veterinary, on_delete=models.RESTRICT)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    pet_name = models.ForeignKey(Pet, on_delete=models.RESTRICT)
    description = models.TextField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=BOOKING_STATUS, default="p")

    class Meta:
        ordering = ["create_date"]

    def __str__(self):
        return self.pet_name.name + "-" + self.owner.username

    def get_absolute_url(self):
        return reverse("veterinary-instance-detail", args=[str(self.id)])
