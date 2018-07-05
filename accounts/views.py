from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views import generic
from django.views.generic import View
from .forms import SignupForm

def index(request):
    return render(request, 'a.html')

#def signup(request):
 #   return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

class UserFormView(View):
    form_class =SignupForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def poet(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.save()
