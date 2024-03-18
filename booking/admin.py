from django.contrib import admin

from booking import models


class SpecialtiesAdmin(admin.ModelAdmin):
    pass


class DoctorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number"]
    empty_value_display = "-empty-"
    search_fields = ["specialties__name"]


class VeterinaryAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "contact_number"]
    search_fields = ["name"]
    ordering = ["name"]


class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "date_birth", "breed"]
    search_fields = ["name", "breed"]
    ordering = ["name"]


class VeterinaryInstanceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "veterinary_name",
        "doctor_name",
        "owner",
        "pet_name",
        "create_date",
        "status",
    ]
    date_hierarchy = "create_date"
    empty_value_display = "-empty-"
    ordering = ["create_date"]


admin.site.register(models.Specialties, SpecialtiesAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Veterinary, VeterinaryAdmin)
admin.site.register(models.VeterinaryInstance, VeterinaryInstanceAdmin)
admin.site.register(models.Pet, PetAdmin)
