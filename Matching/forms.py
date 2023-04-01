'''from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django import forms
from .models import Questions

from django import forms

DEMO_CHOICES =(
	("1", "Female"),
	("2", "Male"),
	("3", "Others"),
)	


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        gender = forms.MultipleChoiceField(choices = DEMO_CHOICES)
        fields = ('age', gender)'''
