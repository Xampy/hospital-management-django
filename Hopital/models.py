from django.db import models

# Create your models here.
class Maladie(models.Model):
    #numero = models.CharField(max_length=100)
    libelle = models.CharField(max_length=100,null=True)


class Medecin(models.Model):
    #numero = models.CharField(max_length=100)
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    dateNaissance = models.DateField(null=True)
    specialite = models.CharField(max_length=100,null=True)
    secteur = models.CharField(max_length=100,null=True)


class Patient(models.Model):
    #numero = models.CharField(max_length=100)
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    dateNaissance = models.DateField(null=True)
    profession = models.CharField(max_length=150,null=True)
    assure = models.BooleanField(default=False)
    assurance = models.CharField(max_length=100,null=True)
    


class Consultation(models.Model):
    #numero = models.CharField(max_length=100)
    dateConsultation = models.DateField(null=True)
    temperature = models.DecimalField(max_digits = 5,decimal_places = 2)
    poids = models.DecimalField(max_digits = 5,decimal_places = 2)
    taille = models.DecimalField(max_digits = 5,decimal_places = 2)
    motif = models.TextField(default="")
    diagnostic = models.TextField(default="")
    actePoser = models.CharField(max_length=100,null=True)

    medecin = models.ForeignKey(Medecin, default=None, null=True, on_delete=models.RESTRICT)
    patient = models.ForeignKey(Patient, default=None, null=True, on_delete=models.RESTRICT )