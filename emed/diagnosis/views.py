from django.views.generic import ListView
from diagnosis.models import Symptom, Disease, Treatment
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader




# class AboutView(TemplateView):
# 	template_name = "about.html"

# class ContactView(TemplateView):
# 	template_name = "contact.html"

class SymptomView(ListView):
	template_name = "diagnosis.html"
	model = Symptom
	context_object_name = "symptom"


class DiagnosisView(View):
	def post():
		if request.method == 'POST':
			symptoms = request.post.getlist('symptoms')

		disease = []
		for i in range(len(symptoms)):
			disease = [e.pk for e in Disease.objects.get(name=symptom[i])]

		treatment =[]
		treatment = Treatment.objects.get(disease=disease)

		return render(request, 'results.html', {"treatment":treatment})










	



