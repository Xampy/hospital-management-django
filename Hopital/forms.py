from django import forms 
from .models import Medecin
from .models import Maladie
from .models import Consultation
from .models import Patient


class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin 
        fields = [
            'nom',
            'prenom',
            'dateNaissance',
            'specialite',
            'secteur'
        ]
    def __init__(self, *args, **kwargs):
        super(MedecinForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder': 'nom du medecin...'}
        )
        self.fields['prenom'].widget.attrs.update({'class' : 'form-control'})
        self.fields['dateNaissance'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )
        self.fields['specialite'].widget.attrs.update({'class' : 'form-control'})
        self.fields['secteur'].widget.attrs.update({'class' : 'form-control'})


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient 
        fields = [
            'nom',
            'prenom',
            'dateNaissance',
            'profession',
            'assure',
            'assurance'
        ]


class ConsultationForm(forms.ModelForm):

    medecin_set = []
    patient_set = []

    query_set = Medecin.objects.all()
    for me in query_set:
        medecin_set.append( (me.pk, me.nom + " " + me.prenom) )

    query_set = Patient.objects.all()
    for pa in query_set:
        patient_set.append( (pa.pk, pa.nom + " " + pa.prenom) )

    medecin_traitant = forms.ChoiceField(choices=medecin_set)
    patient_traite = forms.ChoiceField(choices=patient_set)

    class Meta:
        model = Consultation 
        #exclude = ('medecin', 'patient', )
        fields = [
            #'dateConsultation',
            'temperature',
            'poids',
            'taille',
            'motif',
            'diagnostic',
            'actePoser',
            'medecin',
            'patient'
        ]


    #medecin = forms.ChoiceField(choices=[1, 2, 3, 4])

    def __init__(self, *args, **kwargs):
        super(ConsultationForm, self).__init__(*args, **kwargs)
        """self.fields['dateConsultation'].widget.attrs.update(
            {
                'class' : 'form-control',
                'required': True,
                'type': 'date',
                'placeholder': 
            }
        )"""
        #del self.fields['medecin']
        #del self.fields['medecin']
        self.fields['temperature'].widget.attrs.update(
            {
                'class' : 'form-control',
            },
        )
        self.fields['poids'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )
        self.fields['taille'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )
        self.fields['motif'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )

        self.fields['actePoser'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )

        self.fields['diagnostic'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )
        self.fields['medecin_traitant'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )
        self.fields['patient_traite'].widget.attrs.update(
            {
                'class' : 'form-control',
            }
        )




        self.fields['patient'].widget = forms.HiddenInput()
        self.fields['medecin'].widget = forms.HiddenInput()


        self.fields['medecin'].widget.attrs.update(
            {
                'class' : 'form-control',
                'required': False
            }
        )
        self.fields['patient'].widget.attrs.update(
            {
                'class' : 'form-control',
                'required': False
            }
        )


        

class MaladieForm(forms.ModelForm):
    class Meta:
        model = Maladie 
        fields = [
            'libelle'
        ]

