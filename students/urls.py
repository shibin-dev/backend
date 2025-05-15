
from django.urls import path
from students import views

urlpatterns = [
    path('students/', views.getStudents, name='get_students'),
    path('students/<int:pk>/', views.getStudentDetails, name='get_student_details'),
]
