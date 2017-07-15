from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World!")