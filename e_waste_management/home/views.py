from django.shortcuts import render
#from django.http import HttpResponse


def about(request):
    return render(request,'about.html')
def Index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')

# Create your views here.
