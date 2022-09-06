from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),

    path('user/', views.userPage, name='user-page'),
    path('lesson_user/', views.lessonUser, name='lesson_user'),
    path('lesson_user_view/', views.lessonUserView, name='lesson_user_view'),
    path('notes_user/', views.notesUser, name='notes_user'),
    path('account/', views.accountSettings, name='account'),

    path('lessons/', views.lessons, name='lessons'),

    path('<str:pk>', views.lessonView, name='lesson_view'),
    path('lesson_add/', views.lessonAdd, name='lesson_add'),
    path('lesson_edit/<str:pk>/', views.lessonEdit, name='lesson_edit'),
    path('lesson_delete/<str:pk>/', views.lessonDelete, name='lesson_delete'),
    path('lesson_period/<str:pk>/', views.lessonPeriod, name='lesson_period'),
    path('lesson_period_edit/<str:pk>/', views.lessonPeriodEdit, name='lesson_period_edit'),
    path('lesson_period_add/', views.lessonPeriodAdd, name='lesson_period_add'),

    path('student/', views.student, name='student'),

    path('<str:pk>', views.studentView, name='student_view'),
    path('student_add/', views.studentAdd, name='student_add'),
    path('student_edit/<str:pk>/', views.studentEdit, name='student_edit'),
    path('student_delete/<str:pk>/', views.studentDelete, name='student_delete'),
    path('<str:pk>', views.studentLesson, name='student_lesson'),
    path('notes_student/', views.notesStudent, name='notes_student'),
    path('notes_period/<str:pk>/', views.notesPeriod, name='notes_period'),


    path('notes_create/', views.notesCreate, name='notes_create'),
    path('create_notes/', views.createNotes, name='create_notes'),
    path('update_notes/<str:pk>/', views.updateNotes, name='update_notes'),
    path('delete_notes/<str:pk>/', views.deleteNotes, name='delete_notes'),

    path('update_all_notes/<str:pk>/', views.updateAllNotes, name='update_all_notes'),
    path('create_all_notes/<str:pk>/', views.createAllNotes, name='create_all_notes'),

    path('transkript_user/', views.transkriptUser, name='transkript_user'),
    path('transkript/', views.transkript, name='transkript'),
    path('student_transkript/<str:pk>/', views.studentTranskript, name='student_transkript'),

    path('period/', views.period, name='period'),
]