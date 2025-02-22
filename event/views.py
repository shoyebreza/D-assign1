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

def event(request):
    return render(request, 'event.html')

def blog(request):
    return render(request, 'blog.html')


def gallery(request):
    return render(request, 'gallery.html')

def speaker(request):
    return render(request, 'speaker.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')