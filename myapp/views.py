from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

#kimlik doğrulaması için
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import *

from .forms import NotesForm, StudentForm, DepartmentForm, CreateUserFrom
from .filters import NotesFilter, StudentFilter, DepartmentFilter, LessonFilter

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserFrom()
    if request.method == "POST":
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            """if form.password1 == form.password2:
                if User.objects.filter(username=form.username).exists():
                    messages.info(request, 'Username is already taken')
                    return redirect('register')
                elif User.objects.filter(email=form.email).exists():
                    messages.info(request, 'Email is already taken')
                    return redirect('register')
                else:
                    user = form.save()
            else:
                messages.info(request, 'Both passwords are not matching')
                return redirect('register')"""
            """user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            Student.objects.create(
                user=user,
                name=user.username,
            )"""
            messages.success(request, 'Account was created for' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def index(request):
    department = Department.objects.all()
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    notes = Notes.objects.all()

    total_students = students.count()
    total_departments = department.count()
    total_lesson = lessons.count()


    myFilter = DepartmentFilter(request.GET, queryset=department)
    department = myFilter.qs

    aa = notes.filter(lettergrade='AA').count()
    bb = notes.filter(lettergrade='BB').count()
    ff = notes.filter(lettergrade='FF').count()

    context = {
        'department':department,
        'students':students,
        'lessons':lessons,
        'total_students':total_students,
        'total_departments':total_departments,
        'total_lesson':total_lesson,
        'myFilter':myFilter,
        'aa':aa,
        'bb':bb,
        'ff':ff,
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    notes = request.user.student.notes_set.all()

    notes_count = notes.count()
    aa = notes.filter(lettergrade='AA').count()
    bb = notes.filter(lettergrade='BB').count()
    ff = notes.filter(lettergrade='FF').count()

    context= {
        'notes':notes,
        'aa': aa,
        'bb': bb,
        'ff': ff,
        'notes_count':notes_count,
        }
    return render(request, 'accounts/user.html', context)

login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def lessonUser(request):
    notes = request.user.student.notes_set.all()
    notes_count = notes.count()

    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'notes':notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/lesson_user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def accountSettings(request):
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

#--- department ---

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def department(request, pk):
    department = Department.objects.get(id=pk)
    student = department.student_set.all()

    student_count = student.count()

    myFilter = StudentFilter(request.GET, queryset=student)
    student = myFilter.qs

    context = {
        'student':student,
        'department':department,
        'student_count':student_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/department.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteDepartment(request, pk):
    department = Department.objects.get(id=pk)
    if request.method == "POST":
        department.delete()
        return redirect('/')
    context = {'department':department}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createDepartment(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/department_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateDepartment(request,pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return  redirect('/')
    context = {'form':form}
    return render(request, 'accounts/department_form.html', context)

#--- lesson ---

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessons(request):
    lessons = Lesson.objects.all()

    myFilter = LessonFilter(request.GET, queryset=lessons)
    lessons = myFilter.qs

    total_lesson = lessons.count()

    context = {
        'lessons':lessons,
        'total_lesson':total_lesson,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/lesson.html', context)


#--- student ---


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def students(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()

    aa = notes.filter(lettergrade='AA').count()
    bb = notes.filter(lettergrade='BB').count()
    ff = notes.filter(lettergrade='FF').count()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'student':student,
        'notes':notes,
        'department':department,
        'aa': aa,
        'bb': bb,
        'ff': ff,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('/')
    context = {'student':student}
    return render(request, 'accounts/student_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateStudent(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return  redirect('/')
    context = {'form':form}
    return render(request, 'accounts/student_form.html', context)


#--- notes ---

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createNotes(request, pk):
    NotesFormSet = inlineformset_factory(Student, Notes, fields=('lesson', 'vise', 'final', 'mkexam', 'lettergrade'), extra=5)
    student = Student.objects.get(id=pk)
    formset = NotesFormSet(queryset=Notes.objects.none(), instance=student)
    if request.method == 'POST':
        formset = NotesFormSet(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/notes_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAllNotes(request, pk):
    NotesFormSet = inlineformset_factory(Student, Notes, fields=('lesson', 'vise', 'final', 'mkexam', 'lettergrade'), extra=5)
    student = Student.objects.get(id=pk)
    formset = NotesFormSet(instance=student)
    if request.method == 'POST':
        formset = NotesFormSet(request.POST, instance=student)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/notes_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateNotes(request, pk):
    notes = Notes.objects.get(id=pk)
    form = NotesForm(instance=notes)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/notes_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteNotes(request,pk):
    notes = Notes.objects.get(id=pk)
    if request.method == "POST":
        notes.delete()
        return redirect('/')
    context = {'notes': notes}
    return render(request, 'accounts/notes_delete.html', context)




