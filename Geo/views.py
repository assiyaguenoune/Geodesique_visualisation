from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'Home.html')
def contact(request):
    return render(request,'Contact.html')
def direct(request):
     return render(request,'direct.html')