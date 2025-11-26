from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request, message):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {
        "teachers": teachers,
        "msg": message
    })

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("teachers:list", message="Welcome Teachers!")
    else:
        form = TeacherForm()

    return render(request, "teacher_form.html", {"form": form})
