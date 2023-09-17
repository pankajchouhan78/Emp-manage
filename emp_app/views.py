from django.shortcuts import render , HttpResponse
from .models import Department,Role,Employee
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,"index.html")

def view_all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,"view_all_emp.html",context)

def add_amp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        role = int(request.POST.get('role'))
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))

        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,salary=salary,bonus=bonus,phone=phone,hire_date=datetime.now())

        new_emp.save()
        return HttpResponse("Employee added sucessfully")
    elif request.method == 'GET':
        return render(request,"add_amp.html")
    else:
        return HttpResponse('Something went wrong')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Sucessfully")
        except:
            return HttpResponse("Please Enter A Valid EMP Id")
        
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role= request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request,"view_all_emp.html",context)
    
    elif request.method == 'GET':
        return render(request,"filter_emp.html")
    else:
        return HttpResponse("something went wrong in filter_emp")
