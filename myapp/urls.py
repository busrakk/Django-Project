from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('dashboard-student', views.dashboardStudent, name='dashboard_student'),
    path('dashboard-lesson', views.dashboardLesson, name='dashboard_lesson'),
    path('dashboard-notes', views.dashboardNotes, name='dashboard_notes'),

    path('', views.index, name='index'),

    path('user/', views.userPage, name='user-page'),
    path('lesson_user/', views.lessonUser, name='lesson_user'),
    path('notes_user/', views.notesUser, name='notes_user'),
    path('account/', views.accountSettings, name='account'),

    path('lessons/', views.lessons, name='lessons'),
    path('lesson_delete_page', views.lessonDeletePage, name='lesson_delete_page'),
    path('lesson_update_page', views.lessonUpdatePage, name='lesson_update_page'),
    path('create_lesson/', views.createLesson, name='create_lesson'),
    path('delete_lesson/<str:pk>/', views.deleteLesson, name='delete_lesson'),
    path('update_lesson/<str:pk>/', views.updateLesson, name='update_lesson'),

    path('student/', views.student, name='student'),

    path('<str:pk>', views.studentView, name='student_view'),

    path('add/', views.add, name='add'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),

    path('student_delete_page', views.studentDeletePage, name='student_delete_page'),
    path('student_update_page', views.studentUpdatePage, name='student_update_page'),
    path('create_student/', views.createStudent, name='create_student'),
    path('delete_student/<str:pk>/', views.deleteStudent, name='delete_student'),
    path('update_student/<str:pk>/', views.updateStudent, name='update_student'),

    #path('department/<str:pk>', views.department, name='department'),
    #path('create_department/', views.createDepartment, name='create_department'),
    #path('delete_department/<str:pk>/', views.deleteDepartment, name='delete_department'),
    #path('update_department/<str:pk>/', views.updateDepartment, name='update_department'),

    path('notes/', views.notes, name='notes'),
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
]