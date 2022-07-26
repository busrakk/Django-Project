from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user =models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    num = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(default="user.jpeg", null=True, blank=True)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name

class Period(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lcode = models.CharField(blank=True, max_length=50)
    lname = models.CharField(blank=True, max_length=50)
    lcredit = models.IntegerField(blank=True, null=True)
    period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.lname


class Notes(models.Model):
    STATUS1 = (
        ('gecti', 'Geçti'),
        ('kaldi', 'Kaldı'),
    )
    STATUS2 = (
        ('AA', 'AA'),
        ('BA', 'BA'),
        ('BB', 'BB'),
        ('CB', 'CB'),
        ('CC', 'CC'),
        ('DC', 'DC'),
        ('DD', 'DD'),
        ('FD', 'FD'),
        ('FF', 'FF'),
    )
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    vise = models.IntegerField(null=True, blank=True)
    final = models.IntegerField(null=True, blank=True)
    mkexam = models.IntegerField(null=True, blank=True)
    lettergrade = models.CharField(max_length=2, null=True, choices=STATUS2)
    ort = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=5, null=True, choices=STATUS1)

