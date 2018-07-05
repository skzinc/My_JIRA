from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CompanyEntryForm
from .models import Company

def index(request):
    company = Company.objects.all()
    context = {
        'company': company
    }
    return render(request, 'index.html', context)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CompanyEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CompanyEntryForm()

    return render(request, 'create.html', {'form': form})

def delete(request, id):
    company_entry = Company.objects.get(id=id)
    company_entry.delete()


    return redirect('/')

def update(request, id):
    company_entry = get_object_or_404(Company, id=id)
    #form = CompanyEntryForm(request.POST or None, company_entry=company_entry)
    if request.method == 'POST':
        form = CompanyEntryForm(request.POST, instance=company_entry)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')

    else:
        form = CompanyEntryForm(instance=company_entry)
        # print(form)

    return render(request, 'edit_company_page.html', {'form': form, 'company_entry':company_entry})

