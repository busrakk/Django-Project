from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='index'),

    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),

    path('lessons/', views.lessons, name='lessons'),

    path('students/<str:pk>/', views.students, name='students'),
    path('delete_student/<str:pk>/', views.deleteStudent, name='delete_student'),
    path('update_student/<str:pk>/', views.updateStudent, name='update_student'),

    path('department/<str:pk>', views.department, name='department'),
    path('create_department/', views.createDepartment, name='create_department'),
    path('delete_department/<str:pk>/', views.deleteDepartment, name='delete_department'),
    path('update_department/<str:pk>/', views.updateDepartment, name='update_department'),

    path('create_notes/<str:pk>/', views.createNotes, name='create_notes'),
    path('update_all_notes/<str:pk>/', views.updateAllNotes, name='update_all_notes'),
    path('update_notes/<str:pk>/', views.updateNotes, name='update_notes'),
    path('delete_notes/<str:pk>/', views.deleteNotes, name='delete_notes'),
]