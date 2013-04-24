from django.contrib import admin
from diagnosis.models import Symptom, Disease, Doctor

class SymptomAdmin(admin.ModelAdmin):
	list_display = ('name', 'weight')

class DiseaseAdmin(admin.ModelAdmin):
	list_display = ('name', 'symptom1', 'symptom2', 'symptom3')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('name', 'contact', 'domain')


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Doctor, DoctorAdmin)


