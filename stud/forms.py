from django import forms
from .models import suiv_serv
from adm.models import User

class ServiceForm(forms.ModelForm):
    class Meta:
        model = suiv_serv
        fields = ['type_service', 'nm_user']

    def save(self, commit=True):
        suiv_serv = super(ServiceForm, self).save(commit=False)
        suiv_serv.type_service = self.is_service
        suiv_serv.nm_user = self.id
        if commit:
            suiv_serv.save()

        return suiv_serv




  

    