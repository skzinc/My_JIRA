from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import EmployeeEntryForm
from .models import Employee

def index(request):
    employee = Employee.objects.all()

    context = {
        'employee': employee
    }
    return render(request, 'employee_home.html', context)

def employee_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/employee')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeEntryForm()

    return render(request, 'employee_entry_form.html', {'form': form})

def delete(request, id):
    employee_entry = Employee.objects.get(id=id)
    employee_entry.delete()


    return redirect('/employee')