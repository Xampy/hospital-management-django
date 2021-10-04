from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 

from .models import Medecin
from .forms import MedecinForm

from .models import Maladie
from .forms import MaladieForm

from .models import Consultation
from .forms import ConsultationForm

from .models import Patient
from .forms import PatientForm

# Create your views here.
def ajout_medecin_view(request):
	form = MedecinForm(request.POST or None)

	if form.is_valid():
		form.save()
		return list_medecin_view(request)

	context = {
		'form': form
	}
	return render(request, "medecin/ajout_medecin.html", context)

def list_medecin_view(request):
	# queryset allow to get the list of objects in the database
	queryset = Medecin.objects.all()

	context = {
		"list_medecin": queryset
	}
	return render(request, "medecin/liste_medecin.html", context)



def ajout_patient_view(request):
	form = PatientForm(request.POST or None)

	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "patient/ajout_patient.html", context)

def list_patient_view(request):
	# queryset allow to get the list of objects in the database
	queryset = Patient.objects.all()

	context = {
		"list_patient": queryset
	}
	return render(request, "patient/liste_patient.html", context)










def ajout_consultation_view(request):
	form = ConsultationForm(request.POST or None)

	if form.is_valid():
		medecin = Medecin.objects.get(pk=int(form.data['medecin']))
		patient = Patient.objects.get(pk=int(form.data['patient']))

		data = form.cleaned_data
		print(medecin, patient, data)

		consultation = Consultation()

		consultation.medecin = medecin
		consultation.patient = patient
		consultation.dateConsultation = data['dateConsultation']
		consultation.temperature = data['temperature']
		consultation.poids = data['poids']
		consultation.taille = data['taille']
		consultation.motif = data['motif']
		consultation.diagnostic = data['diagnostic']
		consultation.actePoser = data['actePoser']	
		print(consultation)
        #form.save()"""

	context = {
		'form': form
	}
	return render(request, "consultation/ajout_consultation.html", context)

def list_consultation_view(request):
	# queryset allow to get the list of objects in the database
	query_set = None

	if request.GET.get('action') == "search":
		fil = request.GET.get('filter')
		query = request.GET.get('query')
		queryset = Consultation.objects.filter(motif__contains=query)
	else:
		queryset = Consultation.objects.all()

	context = {
		"list_consultation": queryset
	}
	return render(request, "consultation/liste_consultation.html", context)


def detail_consultation_view(request, id):
	consultation = Consultation.objects.get(pk=int(id))

	context = {
		"consultation": consultation
	}
	return render(request, "consultation/detail_consultation.html", context)







def ajout_maladie_view(request):
	form = MaladieForm(request.POST or None)

	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "maladie/ajout_maladie.html", context)

def list_maladie_view(request):
	# queryset allow to get the list of objects in the database
	queryset = Maladie.objects.all()

	context = {
		"list_maladie": queryset
	}
	return render(request, "maladie/liste_maladie.html", context)




# Create your views here.
def accueil_view(request, *args, **kwargs):
	#print(args, kwargs)
	#print(request.user)

	#return HttpResponse("<h1>Welcome to my django application</h1>")
	return render(request, "accueil.html") # allow to go and take template


def apropos_view(request, *args, **kwargs):
	my_context = {
		
	}
	return render(request, "apropos.html", my_context)
