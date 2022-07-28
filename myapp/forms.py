from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user', 'department']
        labels = {
            'num': 'Student Number',
            'name': 'Student Name',
            'surname': 'Student Surname',
            'grade' : 'Grade'
        }
    widgets = {
        'num': forms.NumberInput(attrs={'class':'form-control'}),
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'surname': forms.TextInput(attrs={'class':'form-control'}),
        'grade': forms.NumberInput(attrs={'class':'form-control'}),
    }

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']