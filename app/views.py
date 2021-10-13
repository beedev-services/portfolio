from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def current(request):
    return render(request, 'main/current.html')

def past(request):
    return render(request, 'main/past.html')
    
def allProjects(request):
    return render(request, 'allProjects.html')

def frontEnd(request):
    return render(request, 'allProjects/frontEnd.html')