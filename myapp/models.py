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
    profile_pic = models.ImageField(default="ubuntu.jpeg", null=True, blank=True)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lcode = models.CharField(blank=True, max_length=50)
    lname = models.CharField(blank=True, max_length=50)
    lcredit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.lname

class Notes(models.Model):
    STATUS = (
        ('AA', 'AA'),
        ('BB', 'BB'),
        ('FF', 'FF'),
    )
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL)
    vise = models.IntegerField(null=True, blank=True)
    final = models.IntegerField(null=True, blank=True)
    mkexam = models.IntegerField(null=True, blank=True)
    lettergrade = models.CharField(max_length=2, null=True, choices=STATUS)

    def __str__(self):
        return self.lesson.lname