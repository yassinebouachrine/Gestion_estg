from django import forms
from .models import Cours
from adm.models import User
from stud.models import Notes


class coursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['nm_cours', 'filiere_cours', 'cours_pdf', 'niv_cours', 'matiere']

    def __init__(self, *args, **kwargs):
        super(coursForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
        
    def save(self, commit=True, user=None):
        Cours = super(coursForm, self).save(commit=False)
        Cours.nm_cours = self.cleaned_data['nm_cours']
        Cours.filiere_cours = self.cleaned_data['filiere_cours']
        Cours.cours_pdf = self.cleaned_data['cours_pdf']
        Cours.niv_cours = self.cleaned_data['niv_cours']
        Cours.matiere = self.cleaned_data['matiere']
        Cours.nm_prof = User.username  

        if commit:
          Cours.save()

        return Cours




class notesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['matiere', 'note', 'session', 'Annee_unv', 'semestre', 'niv_notes', 'resultat', 'etud']

    def __init__(self, *args, **kwargs):
        super(notesForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
        
    def save(self, commit=True):
        Notes = super(notesForm, self).save(commit=False)
        Notes.matiere = self.cleaned_data['matiere']
        Notes.note = self.cleaned_data['note']
        Notes.session = self.cleaned_data['session']
        Notes.Annee_unv = self.cleaned_data['Annee_unv']
        Notes.semestre = self.cleaned_data['semestre']
        Notes.niv_notes = self.cleaned_data['niv_notes']
        Notes.resultat = self.cleaned_data['resultat']
        Notes.etud = self.cleaned_data['etud']

        if commit:
          Notes.save()

        return Notes