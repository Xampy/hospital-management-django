"""ProjetHopital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hopital import views

urlpatterns = [
	path('', views.accueil_view, name="accueil"),
	path('apropos/', views.apropos_view, name="apropos"),
    
	path('medecins/', views.list_medecin_view, name="listmedecin"),
	path('medecins/ajout', views.ajout_medecin_view, name="ajoutmedecin"),

    path('patients/', views.list_patient_view, name="listpatient"),
	path('patients/ajout', views.ajout_patient_view, name="ajoutpatient"),

    path('consultations/', views.list_consultation_view, name="listconsultation"),
	path('consultations/ajout', views.ajout_consultation_view, name="ajoutconsultation"),
    path('consultations/detail/<id>', views.detail_consultation_view, name="detailconsultation"),

    path('maladies/', views.list_maladie_view, name="listmaladie"),
	path('maladies/ajout', views.ajout_maladie_view, name="ajoutmaladie"),
   
    path('admin/', admin.site.urls),
]
