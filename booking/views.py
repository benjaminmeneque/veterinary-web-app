from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from booking import forms, models


# doctor views
class DoctorCreate(LoginRequiredMixin, CreateView):
    model = models.Doctor
    fields = ["first_name", "last_name", "specialties", "email", "phone_number"]


class DoctorUpdate(LoginRequiredMixin, UpdateView):
    model = models.Doctor
    fields = ["first_name", "last_name", "specialties", "email", "phone_number"]


class DoctorDetail(DetailView):
    model = models.Doctor


class DoctorList(ListView):
    model = models.Doctor
    paginate_by = 20


# veterinary views
class VeterinaryCreate(LoginRequiredMixin, CreateView):
    model = models.Veterinary
    fields = ["name", "address", "contact_number"]


class VeterinaryUpdate(LoginRequiredMixin, UpdateView):
    model = models.Veterinary
    fields = ["name", "address", "contact_number"]


class VeterinaryDetail(DetailView):
    model = models.Veterinary


class VeterinaryList(ListView):
    model = models.Veterinary
    paginate_by = 20


# pet views
class PetCreate(LoginRequiredMixin, CreateView):
    model = models.Pet
    form_class = forms.PetCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PetUpdate(LoginRequiredMixin, UpdateView):
    model = models.Pet
    form_class = forms.PetCreateForm


class PetDetail(DetailView):
    model = models.Pet


class PetList(ListView):
    model = models.Pet
    paginate_by = 20


# veterinary instance views
class VeterinaryInstanceCreate(LoginRequiredMixin, CreateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "doctor_name", "pet_name", "description"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class VeterinaryInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "doctor_name", "pet_name", "description"]


class VeterinaryInstanceDetail(DetailView):
    model = models.VeterinaryInstance


class VeterinaryInstanceList(ListView):
    model = models.VeterinaryInstance
    paginate_by = 20


# specialties views
class SpecialtiesCreate(LoginRequiredMixin, CreateView):
    model = models.Specialties
    fields = ["name"]


class SpecialtiesDetail(DetailView):
    model = models.Specialties
