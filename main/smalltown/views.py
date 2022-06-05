from django.shortcuts import render

# Create your views here.
#hompage
def home(request):
    return render(request, 'home.html')