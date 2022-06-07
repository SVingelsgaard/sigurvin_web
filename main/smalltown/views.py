from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
#hompage
def home(request):
    if request.method == "POST":
        grocery = request.POST.get("grocery")
        Shoppinglist.objects.create(grocery = grocery, description = "blanch")
        
    myShoppinglist = Shoppinglist.objects.all
    return render(request, "smalltown.html", {"Shoppinglist": myShoppinglist})