from django.views.generic import ListView, TemplateView
from diagnosis.models import Symptom, Disease, Doctor
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context, loader
from django.db.models import Q



class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class UnifSearchView(TemplateView):
    template_name="search-form.html"

class SymptomView(ListView):
    template_name = "diagnosis.html"
    model = Symptom
    context_object_name = "symptom"


class DiagnosisView(View):  
    # def post(self):       
    #   if request.method == 'POST':
    #       symptoms = request.post.getlist('symptoms')

    #   disease = []
    #   for i in range(len(symptoms)):
    #       disease = [e.pk for e in Disease.objects.get(name=symptom[i])]

    #   treatment =[]
    #   treatment = Treatment.objects.get(disease=disease)

    #   return render(request, "results.html", {"treatment":treatment})

    def post(self, request, *args, **kwargs):               
        symptoms = request.POST.getlist('symptoms')     
        qs = []
        f = []
        if symptoms:
            for symptom in symptoms:
                sympk = Symptom.objects.get(name=symptom)
                print sympk.pk
                f = Q(symptom1=sympk.pk) | Q(symptom2=sympk.pk) | Q(symptom3 = sympk.pk)
            print f
            qs = Disease.objects.get(f)
            print qs            
        else:
            qs = []
        return render(request, "results.html", {"qs":qs})

    # def get_queryset(self):
    #   if self.symptom_list:
    #       for symptom in symptom_list:
    #           qs = Disease.objects.get(Q(symptom1=symptom) | Q(symtpom2=symptom) | Q(symptom3=symptom))
    #   else:
    #       qs =[]

    #   return render(request, "results.html", {"qs":qs})


class SearchView(View):
    def post(self, request, *args, **kwargs):
        search_term = request.POST.get('search_term')
        search_term = str(search_term)
        print search_term
        context = {
            'diseases': Disease.objects.filter(name__icontains=search_term),
            'symptoms': Symptom.objects.filter(name__icontains=search_term),
            'doctors': Doctor.objects.filter(name__icontains=search_term)
            }
        print context
        return render(request, "search-results.html", context)







    



