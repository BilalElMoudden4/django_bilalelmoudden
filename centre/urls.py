from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('students/', views.students_list, name='students_list'),
    path('teachers/', views.teachers_list, name='teachers_list'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path('teachers/<int:id>/', views.teacher_detail, name='teacher_detail'),
]
