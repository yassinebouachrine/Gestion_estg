from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class User(AbstractUser):
    Role = (
        ('ADMIN', 'Admin'),
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher')
    )    

    Gender = (
        ('Female', 'Female'),
        ('Male', 'Male')    
    )

    Nm_filiere = (
        ('Informatique','Informatique'),
        ('Management','Management'),
        ('Energie','Energie'),
        ('Electrique','Electrique'),
    )

    Niv_stud = (
        ('Premiere annee','Premiere annee'),
        ('Deuxième annee','Deuxième annee'),
        ('Troisième annee','Troisième annee'),
    )
    
    
    role = models.CharField(max_length=50, choices=Role)
    filiere = models.CharField(max_length=50, choices=Nm_filiere, default=False)
    gender = models.CharField(max_length=50, choices=Gender, null=True)
    niv_stud = models.CharField(max_length=50, choices=Niv_stud, null=True, default='')

    def __str__(self):
        return self.username



class PDFFile(models.Model):

    Title = (
        ('Informatique','Informatique'),
        ('Management','Management'),
        ('Energie','Energie'),
        ('Electrique','Electrique'),
    )

    Emp_role = (
        ('STUDENT','student'),
        ('TEACHER','teacher'),
    )

    Niv_emp = (
        ('Premiere annee','Premiere annee'),
        ('Deuxième annee','Deuxième annee'),
        ('Troisième annee','Troisième annee'),
    )


    emp_filiere = models.CharField(max_length=200, null=None, default=False, choices=Title)
    pdf_file = models.FileField(upload_to='pdfsEmp/')
    emp_role = models.CharField(max_length=50, default=False, choices=Emp_role)
    niv_emp = models.CharField(max_length=200, default=False, choices=Niv_emp)
    nm_prof = models.CharField(max_length=200, default='')
        


class examens(models.Model):
    Exam_filiere = (
        ('Informatique','Informatique'),
        ('Management','Management'),
        ('Energie','Energie'),
        ('Electrique','Electrique'),
    )

    Niv_filiere = (
        ('Premiere annee','Premiere annee'),
        ('Deuxième annee','Deuxième annee'),
        ('Troisième annee','Troisième annee'),
    )

    Nm_exam = (
        ('DS1','DS1'),
        ('DS2','DS2'),
    )

    nm_exam = models.CharField(max_length=200, null=None, default=False, choices=Nm_exam)
    exam_filiere = models.CharField(max_length=200,  default=False, choices=Exam_filiere)
    niv_filiere = models.CharField(max_length=200, default=False, choices=Niv_filiere)
    conv_exam = models.FileField(upload_to='pdfsExam/')



