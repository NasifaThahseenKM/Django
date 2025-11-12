from django.shortcuts import render

def employdir(request):
    employ = [
        {'name': 'John', 'job_title': 'Developer', 'salary': '100000', 'full_time': True},
        {'name': 'Jane', 'job_title': 'Designer', 'salary': '90000', 'full_time': False},
        {'name': 'Bob', 'job_title': 'Manager', 'salary': '110000', 'full_time': True}
    ]
   
    return render(request, 'employdir.html', {'employ': employ})

