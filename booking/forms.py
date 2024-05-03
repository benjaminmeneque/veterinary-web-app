from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from booking import models


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ["name", "date_birth", "breed"]
        widgets = {
            "date_birth": forms.DateInput(attrs={"type": "date"}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.VeterinaryInstance
        fields = ["veterinary_name", "pet_name", "description", "schedule"]
        widgets = {
            "schedule": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_schedule(self):
        data = self.cleaned_data["schedule"]
        if data < now():
            raise ValidationError("schedule should be in the past")
        return data
