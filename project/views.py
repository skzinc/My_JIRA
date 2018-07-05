from .models import Project, Project_Modules
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ProjectEntryForm, Project_ModuleEntryForm


def index(request):
    project = Project.objects.all()
    project_module = Project_Modules.objects.all()

    context = {
        'project': project,
        'project_module': project_module
    }
    return render(request, 'project_home.html', context)

def project_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/project')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectEntryForm()

    return render(request, 'project_entry_form.html', {'form': form})

def p_module_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Project_ModuleEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/project')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Project_ModuleEntryForm()

    return render(request, 'project_module_entry_form.html', {'form': form})

def delete_project(request, id):
    project_entry = Project.objects.get(id=id)
    project_entry.delete()


    return redirect('/project')

def delete_module(request, id):
    module_entry = Project_Modules.objects.get(id=id)

    module_entry.delete()

    return redirect('/project')
