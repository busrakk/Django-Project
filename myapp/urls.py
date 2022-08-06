from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),

    path('user/', views.userPage, name='user-page'),
    path('lesson_user/', views.lessonUser, name='lesson_user'),
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

    path('lesson_delete_page', views.lessonDeletePage, name='lesson_delete_page'),
    path('lesson_update_page', views.lessonUpdatePage, name='lesson_update_page'),
    path('create_lesson/', views.createLesson, name='create_lesson'),
    path('delete_lesson/<str:pk>/', views.deleteLesson, name='delete_lesson'),
    path('update_lesson/<str:pk>/', views.updateLesson, name='update_lesson'),

    path('student/', views.student, name='student'),

    path('<str:pk>', views.studentView, name='student_view'),
    path('student_add/', views.studentAdd, name='student_add'),
    path('student_edit/<str:pk>/', views.studentEdit, name='student_edit'),
    path('student_delete/<str:pk>/', views.studentDelete, name='student_delete'),
    path('<str:pk>', views.studentLesson, name='student_lesson'),

    path('student_delete_page', views.studentDeletePage, name='student_delete_page'),
    path('student_update_page', views.studentUpdatePage, name='student_update_page'),
    path('create_student/', views.createStudent, name='create_student'),
    path('delete_student/<str:pk>/', views.deleteStudent, name='delete_student'),
    path('update_student/<str:pk>/', views.updateStudent, name='update_student'),

    #path('department/<str:pk>', views.department, name='department'),
    #path('create_department/', views.createDepartment, name='create_department'),
    #path('delete_department/<str:pk>/', views.deleteDepartment, name='delete_department'),
    #path('update_department/<str:pk>/', views.updateDepartment, name='update_department'),

    path('notes_lesson/', views.notesLesson, name='notes_lesson'),
    path('notes_student/', views.notesStudent, name='notes_student'),
    path('notes_period/<str:pk>/', views.notesPeriod, name='notes_period'),


    path('notes_create/', views.notesCreate, name='notes_create'),
    path('notes_update/', views.notesUpdate, name='notes_update'),
    path('notes_delete/', views.notesDelete, name='notes_delete'),
    path('notes_delete_page', views.notesDeletePage, name='notes_delete_page'),
    path('notes_update_page', views.notesUpdatePage, name='notes_update_page'),
    path('create_notes/', views.createNotes, name='create_notes'),
    #path('update_all_notes/<str:pk>/', views.updateAllNotes, name='update_all_notes'),
    path('update_notes/<str:pk>/', views.updateNotes, name='update_notes'),
    path('delete_notes/<str:pk>/', views.deleteNotes, name='delete_notes'),

    path('student_notes_delete/<str:pk>/', views.studentNotesDelete, name='student_notes_delete'),
    path('student_notes_update/<str:pk>/', views.studentNotesUpdate, name='student_notes_update'),
    path('student_notes_view/<str:pk>/', views.studentNotesView, name='student_notes_view'),
    path('student_notes_create/<str:pk>/', views.studentNotesCreate, name='student_notes_create'),

    path('update_all_notes/<str:pk>/', views.updateAllNotes, name='update_all_notes'),

    path('transkript/', views.transkript, name='transkript'),
    path('transkript_pdf/', views.transkript_pdf, name='transkript_pdf'),
    path('pdf_view/', views.ViewPDF.as_view(), name='pdf_view'),
    path('pdf_download/', views.DownloadPDF.as_view(), name='pdf_download'),
    path('student_transkript/<str:pk>/', views.studentTranskript, name='student_transkript'),

    path('period/', views.period, name='period'),
]