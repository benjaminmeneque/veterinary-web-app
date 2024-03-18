from django import forms

from booking import models


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = models.Pet
        fields = ["name", "date_birth", "breed"]
        widgets = {
            "date_birth": forms.DateInput(attrs={"type": "date"}),
        }
