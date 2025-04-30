from django.db import models
from adm.models import User

# Create your models here.


class Cours(models.Model):
    Filiere_cours = (
        ('Informatique','Informatique'),
        ('Management','Management'),
        ('Energie','Energie'),
        ('Electrique','Electrique'),
    )

    Niv_cours = (
        ('Premiere annee','Premiere annee'),
        ('Deuxième annee','Deuxième annee'),
        ('Troisième annee','Troisième annee'),
    )

    nm_cours = models.CharField(max_length=200, null=None)
    nm_prof = models.CharField(max_length=150, null=None)
    filiere_cours = models.CharField(max_length=200, choices=Filiere_cours)
    cours_pdf = models.FileField(upload_to='pdfscours/')
    niv_cours = models.CharField(max_length=200, choices=Niv_cours)
    matiere = models.CharField(max_length=200)

    def __str__(self):
        return self.id

