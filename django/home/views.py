from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from .forms import StudentCreateForm, StudentUpdateForm
# Create your views here.


def home(request):
    all = Student.objects.all()
    return render(request, 'home.html', {'students': all})


def detail(request, st_id):
    stu = Student.objects.get(un_id=st_id)
    return render(request, 'detail.html',{'stu': stu})

def delete(request, st_id):
    Student.objects.get(id=st_id).delete()
    messages.success(request, 'Student deleted succesfully!', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            # Student.objects.create(name = cd['name'], subject=cd['subject'] , verify_date= cd['verify_date'], un_id = cd['un_id'])
            Student.objects.create(name=cd['name'], subject=cd['subject'], verify_date=cd['verify_date'], un_id=cd['un_id'])

            messages.success(request, 'Student add successfully!', 'success')
            return redirect('home')
    else:
        form = StudentCreateForm()
        return render(request, 'create.html', {'form': form})
    



def update(request, st_id):
    student = Student.objects.get(id = st_id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance= student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!', 'success')
            return redirect('details', st_id) 
    else:
        form = StudentUpdateForm(instance=student)
        return render(request, 'update.html', {'form': form})