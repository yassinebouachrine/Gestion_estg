from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model




class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2','email']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = 'ADMIN'
        if commit:
            user.save()

        return user


class SignUpFormstud(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField()
    filiere = forms.CharField()
    niv_stud = forms.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'gender', 'email', 'filiere', 'niv_stud']

    def save(self, commit=True):
        user = super(SignUpFormstud, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = 'STUDENT'        
        user.gender = self.cleaned_data['gender']
        user.filiere = self.cleaned_data['filiere']
        user.niv_stud = self.cleaned_data['niv_stud']
        if commit:
            user.save()

        return user
 

class SignUpFormprof(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.CharField()
    filiere = forms.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'gender', 'email', 'filiere']

    def save(self, commit=True):
        user = super(SignUpFormprof, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = 'TEACHER'
        user.gender = self.cleaned_data['gender']
        user.filiere = self.cleaned_data['filiere']
        if commit:
            user.save()

        return user




from .models import PDFFile, examens

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['emp_filiere', 'pdf_file', 'nm_prof']

    def __init__(self, *args, **kwargs):
        super(PDFFileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' 

    def save(self, commit=True):
        PDFFile = super(PDFFileForm, self).save(commit=False)
        PDFFile.emp_filiere = self.cleaned_data['emp_filiere']
        PDFFile.nm_prof = self.cleaned_data['nm_prof']
        PDFFile.pdf_file = self.cleaned_data['pdf_file']
        PDFFile.emp_role = 'TEACHER'
        PDFFile.niv_emp = 'FALSE'
        if commit:
            PDFFile.save()

        return PDFFile




class PDFFileForm1(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['emp_filiere', 'pdf_file', 'niv_emp']

    def __init__(self, *args, **kwargs):
        super(PDFFileForm1, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' 

    def save(self, commit=True):
        PDFFile = super(PDFFileForm1, self).save(commit=False)
        PDFFile.emp_filiere = self.cleaned_data['emp_filiere']
        PDFFile.nm_prof = 'FALSE'
        PDFFile.pdf_file = self.cleaned_data['pdf_file']
        PDFFile.emp_role = 'STUDENT'
        PDFFile.niv_emp = self.cleaned_data['niv_emp']
        if commit:
            PDFFile.save()

        return PDFFile    
        



class examensForm(forms.ModelForm):
    class Meta:
        model = examens
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(examensForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' 


