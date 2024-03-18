from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from booking import forms, models


class DoctorCreate(LoginRequiredMixin, CreateView):
    model = models.Doctor
    fields = ["first_name", "last_name", "specialties", "email", "phone_number"]


class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = models.Doctor
    fields = ["first_name", "last_name", "specialties", "email", "phone_number"]


class VeterinaryCreate(LoginRequiredMixin, CreateView):
    model = models.Veterinary
    fields = ["name", "address", "contact_number"]


class VeterinaryUpdate(LoginRequiredMixin, UpdateView):
    model = models.Veterinary
    fields = ["name", "address", "contact_number"]


class PetCreate(LoginRequiredMixin, CreateView):
    model = models.Pet
    form_class = forms.PetCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PetUpdate(LoginRequiredMixin, UpdateView):
    model = models.Pet
    form_class = forms.PetCreateForm


class VeterinaryInstanceCreate(LoginRequiredMixin, CreateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "doctor_name", "pet_name", "description"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class VeterinaryInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "doctor_name", "pet_name", "description"]


class SpecialtiesCreate(LoginRequiredMixin, CreateView):
    model = models.Specialties
    fields = ["name"]
