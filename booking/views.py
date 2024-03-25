from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from booking import forms, models


# index view
def index(request):
    available_clinics = models.Veterinary.objects.count()
    available_doctors = models.Doctor.objects.count()
    num_pets = 0
    num_appointments = 0

    if request.user.is_authenticated:
        num_pets = models.Pet.objects.filter(owner=request.user).count()
        num_appointments = models.VeterinaryInstance.objects.filter(
            owner=request.user
        ).count()

    context = {
        "available_clinics": available_clinics,
        "available_doctors": available_doctors,
        "num_pets": num_pets,
        "num_appointments": num_appointments,
    }
    return render(request, "index.html", context=context)


# staff views
def ApppoinmentsView(request):
    pending_appointments = models.VeterinaryInstance.objects.filter(status="p")
    approved_appointments = models.VeterinaryInstance.objects.filter(status="a")
    declined_appointments = models.VeterinaryInstance.objects.filter(status="d")

    context = {
        "pending_appointments": pending_appointments,
        "approved_appointments": approved_appointments,
        "declined_appointments": declined_appointments,
    }
    return render(request, "booking/appointments.html", context=context)


# doctor views
class DoctorCreate(LoginRequiredMixin, CreateView):
    model = models.Doctor
    fields = [
        "first_name",
        "last_name",
        "clinic",
        "specialties",
        "email",
        "phone_number",
    ]


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
    fields = ["name", "address", "contact_number", "services"]


class VeterinaryUpdate(LoginRequiredMixin, UpdateView):
    model = models.Veterinary
    fields = ["name", "address", "contact_number", "services"]


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


class PetList(LoginRequiredMixin, ListView):
    model = models.Pet
    paginate_by = 20

    def get_queryset(self):
        pet_list = models.Pet.objects.filter(owner=self.request.user)
        return pet_list


# veterinary instance views
class VeterinaryInstanceCreate(LoginRequiredMixin, CreateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "pet_name", "description"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filter pet_name field choices based on the logged-in user
        form.fields["pet_name"].queryset = models.Pet.objects.filter(
            owner=self.request.user
        )
        return form


class VeterinaryInstanceUpdate(LoginRequiredMixin, UpdateView):
    model = models.VeterinaryInstance
    fields = ["veterinary_name", "doctor", "description", "status"]


class VeterinaryInstanceDetail(DetailView):
    model = models.VeterinaryInstance


class VeterinaryInstanceList(LoginRequiredMixin, ListView):
    model = models.VeterinaryInstance
    paginate_by = 20

    def get_queryset(self):
        booking_list = models.VeterinaryInstance.objects.filter(owner=self.request.user)
        return booking_list


# specialties views
class SpecialtiesCreate(LoginRequiredMixin, CreateView):
    model = models.Specialties
    fields = ["name"]


class SpecialtiesDetail(DetailView):
    model = models.Specialties


class SearchResultsList(ListView):
    model = models.Veterinary
    template_name = "booking/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = models.Veterinary.objects.filter(
                Q(name__icontains=query) | Q(address__icontains=query)
            )

            return object_list


# services
class CreateService(CreateView):
    model = models.Service
    fields = ["name"]
    success_url = reverse_lazy("service-create")
