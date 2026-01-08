from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'urgency_score', 'risk_score', 'reward_score']
        
        widgets = {
            'urgency_score': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'risk_score': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'reward_score': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }