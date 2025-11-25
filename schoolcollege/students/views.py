from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, "home.html", {"students": students})

def result_page(request, student_name):
    student = get_object_or_404(Student, name=student_name)
    return render(request, "result.html", {"student": student})
