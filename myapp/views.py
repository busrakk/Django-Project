import datetime

from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm

#kimlik doğrulaması için
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.urls import reverse

from .models import *

from .forms import NotesForm, StudentForm, LessonForm, CreateUserFrom
from .filters import NotesFilter, StudentFilter, LessonFilter, PeriodFilter

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

#-----------------------------------------------------



#------------------------------------------------------

# -------------- signup & login ------------
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

#----------- dashboard ------------

@login_required(login_url='login')
@admin_only
def index(request):
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    notes = Notes.objects.all()

    total_students = students.count()
    total_lesson = lessons.count()
    total_notes = notes.count()

    context = {
        'students':students,
        'lessons':lessons,
        'notes':notes,
        'total_notes':total_notes,
        'total_students':total_students,
        'total_lesson':total_lesson,
    }

    return render(request, 'accounts/dashboard.html', context)


#------------ User Page ------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    notes = request.user.student.notes_set.all()


    notes_count = notes.count()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    context= {
        'notes':notes,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
        'notes_count':notes_count,
        }
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def lessonUser(request):
    period = Period.objects.all()
    lesson = Lesson.objects.all()

    myFilter = LessonFilter(request.GET, queryset=lesson)
    lesson = myFilter.qs

    context = {
        'period': period,
        'lesson': lesson,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/lesson_user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def lessonUserView(request):
    notes = request.user.student.notes_set.all()
    notes_count = notes.count()

    period = Period.objects.all()

    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs


    context = {
        'notes':notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
        'period':period,
    }
    return render(request, 'accounts/lesson_user_view.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def notesUser(request):
    notes = request.user.student.notes_set.all()
    notes_count = notes.count()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'notes':notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
    }
    return render(request, 'accounts/notes_user.html', context)

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


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def transkriptUser(request):
    notes = request.user.student.notes_set.all()
    notes_count = notes.count()

    period = Period.objects.all()
    context = {
        'notes':notes,
        'notes_count':notes_count,
        'period':period,
    }
    return render(request, 'accounts/transkript_user.html', context)


#-------------- lesson ------------


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessons(request):
    lessons = Lesson.objects.all()
    lesson_count = lessons.count()

    myFilter = LessonFilter(request.GET, queryset=lessons)
    lessons = myFilter.qs

    total_lesson = lessons.count()

    context = {
        'lessons':lessons,
        'lesson_count':lesson_count,
        'total_lesson':total_lesson,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/lesson_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonView(request,pk):
    i = Lesson.objects.get(id=pk)
    return HttpResponseRedirect(reverse('period'))


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonAdd(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            new_code = form.cleaned_data['lcode']
            new_name = form.cleaned_data['lname']
            new_credit = form.cleaned_data['lcredit']
            new_period = form.cleaned_data['period']

            new_lesson = Lesson(
                lcode = new_code,
                lname = new_name,
                lcredit = new_credit,
                period = new_period,
            )
            new_lesson.save()
            return render(request, 'accounts/add_lesson.html', {
                              'form':LessonForm(),
                              'success':True,
                          })
    else:
        form = LessonForm()
    return render(request, 'accounts/add_lesson.html', {
         'form':LessonForm
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonEdit(request, pk):
    if request.method == 'POST':
        lesson = Lesson.objects.get(id=pk)
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/edit_lesson.html', {
                'form':form,
                'success':True,
            })
    else:
        lesson = Lesson.objects.get(id=pk)
        form = LessonForm(instance=lesson)
    return render(request, 'accounts/edit_lesson.html', {
        'form':form,
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonDelete(request, pk):
    if request.method == 'POST':
        lesson = Lesson.objects.get(id=pk)
        lesson.delete()
    return HttpResponseRedirect(reverse('period'))


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonPeriod(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lessons = lesson.student.all()
    notes = lesson.notes_set.all()
    notess = Notes.objects.all()

    myFilter = NotesFilter(request.GET, queryset=notess)
    notess = myFilter.qs

    context = {
        'lessons':lessons,
        'lesson':lesson,
        'notes':notes,
        'notess':notess,
    }
    return render(request, 'accounts/lesson_period.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonPeriodEdit(request, pk):
    if request.method == 'POST':
        notes = Notes.objects.get(id=pk)
        form = NotesForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/lesson_period_edit.html', {
                'form':form,
                'success':True,
            })
    else:
        notes = Notes.objects.get(id=pk)
        form = NotesForm(instance=notes)
    return render(request, 'accounts/lesson_period_edit.html', {
        'form':form,
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonPeriodAdd(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            new_vise = form.cleaned_data['vise']
            new_final = form.cleaned_data['final']
            new_mkexam = form.cleaned_data['mkexam']
            new_lettergrade = form.cleaned_data['lettergrade']

            new_note = Notes(
                vise = new_vise,
                final = new_final,
                mkexam = new_mkexam,
                lettergrade = new_lettergrade,
            )
            new_note.save()
            return render(request, 'accounts/add_notes.html', {
                              'form':NotesForm(),
                              'success':True,
                          })
    else:
        form = NotesForm()
    return render(request, 'accounts/add_notes.html', {
         'form':NotesForm
    })

#--------------- end of lesson model -------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonDeletePage(request):
    lessons = Lesson.objects.all()
    lesson_count = lessons.count()

    myFilter = LessonFilter(request.GET, queryset=lessons)
    lessons = myFilter.qs

    context = {
        'lessons': lessons,
        'lesson_count':lesson_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/lesson_delete_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def lessonUpdatePage(request):
    lesson = Lesson.objects.all()
    lesson_count = lesson.count()

    myFilter = LessonFilter(request.GET, queryset=lesson)
    lesson = myFilter.qs

    context = {
        'lesson': lesson,
        'lesson_count':lesson_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/lesson_update_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createLesson(request):
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lessons')
    context = {'form':form}
    return render(request, 'accounts/lesson_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateLesson(request,pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(instance=lesson)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return  redirect('lesson_update_page')
    context = {'form':form}
    return render(request, 'accounts/lesson_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    if request.method == "POST":
        lesson.delete()
        return redirect('lesson_delete_page')
    context = {'lesson':lesson}
    return render(request, 'accounts/lesson_delete.html', context)

#--- student ---

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def student(request):
    students = Student.objects.all()
    student_count = students.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'student_count':student_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/student_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentView(request,pk):
    i = Student.objects.get(id=pk)
    return HttpResponseRedirect(reverse('student'))

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentAdd(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_num = form.cleaned_data['num']
            new_name = form.cleaned_data['name']
            new_surname = form.cleaned_data['surname']
            new_grade = form.cleaned_data['grade']

            new_student = Student(
                num = new_num,
                name = new_name,
                surname = new_surname,
                grade = new_grade,
            )
            new_student.save()
            return render(request, 'accounts/add_student.html', {
                              'form':StudentForm(),
                              'success':True,
                          })
    else:
        form = StudentForm()
    return render(request, 'accounts/add_student.html', {
         'form':StudentForm
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentEdit(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/edit_student.html', {
                'form':form,
                'success':True,
            })
    else:
        student = Student.objects.get(id=pk)
        form = StudentForm(instance=student)
    return render(request, 'accounts/edit_student.html', {
        'form':form,
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentDelete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        student.delete()
    return HttpResponseRedirect(reverse('student'))

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentLesson(request,pk):
    i = Student.objects.get(id=pk)
    notes = student.notes_set.all()
    return HttpResponseRedirect(reverse('notes'))

#--------------- end of student model -------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentDeletePage(request):
    students = Student.objects.all()
    student_count = students.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'student_count':student_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/student_delete_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentUpdatePage(request):
    students = Student.objects.all()
    student_count = students.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'student_count':student_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/student_view.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createStudent(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {'form':form}
    return render(request, 'accounts/student_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_delete_page')
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
            return  redirect('student_update_page')
    context = {'form':form}
    return render(request, 'accounts/student_form.html', context)


#--- notes ---

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesPeriod(request, pk):
    lesson = Lesson.objects.get(id=pk)
    lessons = lesson.student.all()
    notes = lesson.notes_set.all()
    notess = Notes.objects.all()

    myFilter = NotesFilter(request.GET, queryset=notess)
    notess = myFilter.qs

    context = {
        'lessons':lessons,
        'lesson':lesson,
        'notes':notes,
        'notess':notess,
    }
    return render(request, 'accounts/notes_period.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesLesson(request):
    lessons = Lesson.objects.all()
    lessons_count = lessons.count()

    myFilter = LessonFilter(request.GET, queryset=lessons)
    lessons = myFilter.qs

    context = {
        'lessons':lessons,
        'lessons_count': lessons_count,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/notes_lesson.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesStudent(request):
    students = Student.objects.all()
    student_count = students.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'student_count':student_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/notes_student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesCreate(request):
    notes = Notes.objects.all()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'notes': notes,
        'notes_count': notes_count,
        'myFilter': myFilter,
    }
    return render(request, 'accounts/notes_create.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesUpdate(request):
    notes = Notes.objects.all()
    student = Student.objects.all()

    notes_count = notes.count()
    student_count = student.count()

    myFilter = StudentFilter(request.GET, queryset=student)
    student = myFilter.qs

    context = {
        'student':student,
        'student_count':student_count,
        'notes':notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/notes_update_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesDelete(request):
    notes = Notes.objects.all()
    student = Student.objects.all()

    notes_count = notes.count()
    student_count = student.count()

    myFilter = StudentFilter(request.GET, queryset=student)
    student = myFilter.qs

    context = {
        'student':student,
        'student_count':student_count,
        'notes':notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/notes_delete_page.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesDeletePage(request):
    notes = Notes.objects.all()
    notes_count = notes.count()

    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'notes': notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/notes_delete_page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def notesUpdatePage(request):
    notes = Notes.objects.all()
    notes_count = notes.count()

    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'notes': notes,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/notes_update_page.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createNotes(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_create')
    context = {'form': form}
    return render(request, 'accounts/notes_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAllNotes(request, pk):
    NotesFormSet = inlineformset_factory(Lesson, Notes, fields=('student', 'lesson', 'vise', 'final', 'mkexam', 'lettergrade', 'ort', 'status'))
    lesson = Lesson.objects.get(id=pk)
    lessons = lesson.student.all()
    notes = lesson.notes_set.all()
    formset = NotesFormSet(instance=lesson)
    if request.method == 'POST':
        formset = NotesFormSet(request.POST, instance=lesson)
        if formset.is_valid():
            formset.save()
            return redirect('lessons')
    context = {
        'formset':formset,
        'lessons':lessons,
        'notes':notes,
    }
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
            return redirect('notes_update')

    context = {'form':form}
    return render(request, 'accounts/notes_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteNotes(request,pk):
    notes = Notes.objects.get(id=pk)
    if request.method == "POST":
        notes.delete()
        return redirect('notes_delete')
    context = {'notes': notes}
    return render(request, 'accounts/notes_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentNotesDelete(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'student':student,
        'notes':notes,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/student_notes_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentNotesUpdate(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'student':student,
        'notes':notes,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/student_notes_update.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentNotesView(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'student':student,
        'notes':notes,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/student_notes_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentNotesCreate(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    notes_count = notes.count()

    # Student filter
    myFilter = NotesFilter(request.GET, queryset=notes)
    notes = myFilter.qs

    context = {
        'student':student,
        'notes':notes,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
        'notes_count':notes_count,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/student_notes_create.html', context)

#------------- Transkript -------------

"""@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def transkript(request):
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    notes = Notes.objects.all()

    total_students = students.count()
    total_lesson = lessons.count()
    total_notes = notes.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    aa = notes.filter(lettergrade='AA').count()
    ba = notes.filter(lettergrade='BA').count()
    bb = notes.filter(lettergrade='BB').count()
    cb = notes.filter(lettergrade='CB').count()
    cc = notes.filter(lettergrade='CC').count()
    dc = notes.filter(lettergrade='DC').count()
    dd = notes.filter(lettergrade='DD').count()
    fd = notes.filter(lettergrade='FD').count()
    ff = notes.filter(lettergrade='FF').count()

    context = {
        'students': students,
        'lessons': lessons,
        'notes':notes,
        'total_students': total_students,
        'total_lesson': total_lesson,
        'total_notes':total_notes,
        'myFilter': myFilter,
        'aa': aa,
        'ba': ba,
        'bb': bb,
        'cb': cb,
        'cc': cc,
        'dc': dc,
        'dd': dd,
        'fd': fd,
        'ff': ff,
    }
    return render(request, 'accounts/transkript.html', context)"""

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def transkript(request):
    students = Student.objects.all()

    total_students = students.count()

    myFilter = StudentFilter(request.GET, queryset=students)
    students = myFilter.qs

    context = {
        'students': students,
        'total_students': total_students,
        'myFilter': myFilter,

    }
    return render(request, 'accounts/transkript.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def studentTranskript(request, pk):
    student = Student.objects.get(id=pk)
    notes = student.notes_set.all()
    period = Period.objects.all()

    notes_count = notes.count()

    context = {
        'student':student,
        'notes':notes,
        'notes_count':notes_count,
        'period':period,
    }
    return  render(request, 'accounts/transkript_student.html', context)

"""@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def transkriptView(request,pk):
    student = Student.objects.get(id=pk)

    return HttpResponseRedirect(reverse('student_notes_view'))"""



#----------------- period --------------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def period(request):
    period = Period.objects.all()
    lesson = Lesson.objects.all()

    myFilter = LessonFilter(request.GET, queryset=lesson)
    lesson = myFilter.qs

    context = {
        'period':period,
        'lesson':lesson,
        'myFilter':myFilter,
    }
    return  render(request, 'accounts/period.html', context)

