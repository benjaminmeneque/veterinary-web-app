import uuid

from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Specialties(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    specialties = models.ManyToManyField(Specialties)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.last_name + "," + self.first_name


class Veterinary(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    contact_number = PhoneNumberField(blank=False, null=False)

    def __str__(self):
        return self.name


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, blank=False, null=False)
    date_birth = models.DateField()
    breed = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.pet_name.name + "-" + self.owner.username
