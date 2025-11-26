from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request, message):
    students = Student.objects.all()
    return render(request, "student_list.html", {
        "students": students,
        "msg": message
    })

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:list", message="Welcome Students!")
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form})

