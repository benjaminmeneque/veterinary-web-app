from django.contrib import admin

from booking import models


# Register your models here.
class SpecialtiesAdmin(admin.ModelAdmin):
    pass


class DoctorAdmin(admin.ModelAdmin):
    pass


class VeterinaryAdmin(admin.ModelAdmin):
    pass


class PetAdmin(admin.ModelAdmin):
    pass


class VeterinaryInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Specialties, SpecialtiesAdmin)
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Veterinary, VeterinaryAdmin)
admin.site.register(models.VeterinaryInstance, VeterinaryInstanceAdmin)
admin.site.register(models.Pet, PetAdmin)
