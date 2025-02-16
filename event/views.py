from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def faq(request):
    return render(request, 'faq.html')







