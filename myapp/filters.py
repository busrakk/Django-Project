import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class NotesFilter(django_filters.FilterSet):

    class Meta:
        model = Notes
        fields = ['lesson__period']
        exclude = ['student']
        labels = {
            'lesson__period': 'Dönem',
        }

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['profile_pic', 'user', 'department']
        labels = {
            'num': 'Öğrenci Numarası',
            'name': 'Öğrenci Adı',
            'surname': 'Öğrenci Soyadı',
            'grade': 'Öğrenci Sınıfı'
        }


class DepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = Department
        fields = '__all__'


class LessonFilter(django_filters.FilterSet):

    class Meta:
        model = Lesson
        fields = ['period']
        labels = {
            'period': 'Ders Dönemi'
        }

class PeriodFilter(django_filters.FilterSet):

    class Meta:
        model = Period
        fields = ['name']
        labels = {
            'name': 'Ders Dönemi'
        }