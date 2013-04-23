from django.contrib import admin
from diagnosis.models import Symptom, Disease, Treatment

class SymptomAdmin(admin.ModelAdmin):
	list_display = ('name', 'weight')

class DiseaseAdmin(admin.ModelAdmin):
	list_display = ('name', 'symptom1', 'symptom2', 'symptom3')

class TreatmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'disease')


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Treatment, TreatmentAdmin)


