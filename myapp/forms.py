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
            'num': 'Öğrenci Numarası',
            'name': 'Öğrenci Adı',
            'surname': 'Öğrenci Soyadı',
            'grade' : 'Öğrenci Sınıfı',
            'profile_pic': 'Profil Fotoğrafı',
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
        labels = {
            'student': 'Öğrenci Adı',
            'lesson': 'Ders Adı',
            'vise': 'Vize',
            'final': 'Final',
            'mkexam':'Büt',
            'lettergrade':'Harf',
            'ort':'Ort',
            'status':'Durum'
        }
        widgets = {
            'student': forms.TextInput(attrs={'class': 'form-control'}),
            'lesson': forms.Select(attrs={'class': 'form-control'}),
            'vise': forms.NumberInput(attrs={'class': 'form-control'}),
            'final': forms.NumberInput(attrs={'class': 'form-control'}),
            'mkexam': forms.NumberInput(attrs={'class': 'form-control'}),
            'lettergrade': forms.Select(attrs={'class': 'form-control'}),
            'ort': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['student']
        labels = {
            'lcode': 'Ders Kodu',
            'lname': 'Ders Adı',
            'lcredit': 'Ders Kredi',
            'period': 'Ders Dönemi'
        }
        widgets = {
            'lcode': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'lcredit': forms.NumberInput(attrs={'class': 'form-control'}),
            'period': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
