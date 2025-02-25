from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('save_student_name/', views.save_student_name, name='save_student_name'),
]