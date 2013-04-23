from django.views.generic import ListView
from diagnosis.models import Symptom

# class AboutView(TemplateView):
# 	template_name = "about.html"

# class ContactView(TemplateView):
# 	template_name = "contact.html"

class DiagnosisView(ListView):
	template_name = "diagnosis.html"
	model = Symptom
	context_object_name = "symptom"

	