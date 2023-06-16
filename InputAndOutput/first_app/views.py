from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.forms import StudentForm
from first_app.models import StudentModel

# Create your views here.
def home(request):
    student = StudentModel.objects.all()
    return render(request, 'first_app/home.html', {'data': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST or request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('show_student')
    else:
        form = StudentForm()
    return render(request, 'first_app/add_student.html', {'form':form})

def show_student(request):
    student = StudentModel.objects.all()
    return render(request, 'first_app/delete_student.html', {'data' : student})

def delete_student(request, roll):
    student = StudentModel.objects.get(pk = roll).delete()
    print(student)
    return redirect('show_student')
    