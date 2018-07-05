from django import forms
from .models import Project, Project_Modules

class ProjectEntryForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class Project_ModuleEntryForm(forms.ModelForm):
    class Meta:
        model = Project_Modules
        fields = '__all__'
