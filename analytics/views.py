from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class MyView(View):
    def get(self, request):
        return render(request, 'analytics/index.html')

