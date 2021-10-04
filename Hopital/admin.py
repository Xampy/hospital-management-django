from django.contrib import admin

from .models import Medecin,Consultation, Patient, Maladie

# Register your models here.
admin.site.register(Medecin)
admin.site.register(Consultation)
admin.site.register(Patient)
admin.site.register(Maladie)
