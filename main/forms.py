from django import forms
from .models import Question

class TestingForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer']
    