from django import forms
from .models import ResearchProject, ResearchData

class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['title', 'description', 'lead_researcher', 'start_date', 'end_date']

class ResearchDataForm(forms.ModelForm):
    class Meta:
        model = ResearchData
        fields = ['data_file']
