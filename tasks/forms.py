from django import forms
from django.forms import ModelForm
from django.utils import timezone

from .models import *

class TaskFrom(forms.ModelForm):
    
    class Meta:
        model = Task
        fields ='__all__'


