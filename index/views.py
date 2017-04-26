from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import HouseSignupForm, SearchForm
# Create your views here.

class Home(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'index/home.html', {'form': form})

class Signup(View):
    def post(self, request):
        form = HouseSignupForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/signup/complete/')

    def get(self, request):
        form = HouseSignupForm()
        return render(request, 'index/signup.html', {'signup_form': form})

class Login(View):
    def get(self, request):
        return render(request, 'index/login.html')
