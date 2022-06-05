from django.shortcuts import render


#hompage
def home(request):
    return render(request, 'homee.html')
