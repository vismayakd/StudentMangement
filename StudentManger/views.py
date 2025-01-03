from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request,'StudentManager/List.html',{'students':students})

def student_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        grade = request.POST['grade']
        email = request.POST['email']
        Student.objects.create(name=name,age=age,grade=grade,email=email)
        return redirect('student_list')
    return render(request,'StudentManager/StudentAdd.html')

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.grade = request.POST['grade']
        student.email = request.POST['email']
        student.save()
        return redirect('student_list')
    return render(request, 'StudentManager/Edit.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'StudentManager/Delete.html', {'student': student})
