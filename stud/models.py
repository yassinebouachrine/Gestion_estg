from django.db import models
from adm.models import User

# Create your models here.



class Notes(models.Model):
    Resultat = (
        ('V','v'),
        ('R','r'),
    )

    Session = (
        ('1','1'),
        ('2','2'),
    )

    Semestre = (
        ('S1','s1'),
        ('S2','s2'),
        ('S3','s3'),
        ('S4','s4'),
        ('S5','s5'),
        ('S6','s6'),
    )
    Niv_etud = (
        ('Premiere annee','Premiere annee'),
        ('Deuxième annee','Deuxième annee'),
        ('Troisième annee','Troisième annee'),
    )

    id_note = models.AutoField(primary_key=True)
    matiere = models.CharField(max_length=50, default=None)
    resultat = models.CharField(max_length=50, default=None, choices=Resultat)
    session = models.CharField(max_length=50, default=1, choices=Session)
    note = models.FloatField(default=None)
    etud = models.CharField(max_length=50, default=False)
    semestre = models.CharField(max_length=50, default=False, choices=Semestre)
    Annee_unv = models.IntegerField(default=None)
    niv_notes = models.CharField(max_length=200, default=None, choices=Niv_etud)  

    class meta:
        db_table = 'notes'
    
    def __str__(self):
        return self.id_note   


class services(models.Model):

    Type = (
        ('Tuition certificate', 'Tuition certificate'),
        ('transcript', 'transcript'),
        ('Certificate of results', 'Certificate of results'),
        ('Certificate of achievement', 'Certificate of achievement'),
        ('Baccalaureate certified copy', 'Baccalaureate certified copy'),
        ('Provisional Baccalaureate', 'Provisional Baccalaureate'),
        ('Bachelor degree', 'Bachelor degree'),
        ('student card', 'student card'),
        ('Sign a document', 'Sign a document'),
    )


    is_service = models.AutoField(primary_key=True)
    type_s = models.CharField(max_length=50, choices=Type)

    class meta:
        db_table = 'service'
        
    def __str__(self):
        return self.is_service
        


class suiv_serv(models.Model):
    id_service = models.AutoField(primary_key=True)
    type_service = models.ForeignKey(services, null=True, on_delete=models.CASCADE)
    nm_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class meta:
        db_table='suiv_service'
    
     
    def __str__(self):
        return self.id_service



