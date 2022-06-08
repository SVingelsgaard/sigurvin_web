from django.shortcuts import render, redirect
from .models import Shoppinglist

#hompage
def home(request):
    return render(request, "smalltown.html", {"Shoppinglist": Shoppinglist.objects.all})

def add_grocery(request):
    if request.method == "POST":
        grocery = request.POST.get("grocery")
        Shoppinglist.objects.create(grocery = grocery, description = "blanch")
        #shoud make it so i the item is not named shoppinglist
        
    return redirect("home")

def remove_grocery(request):
    if request.method == "POST":
        id = request.POST.get("Shopping")
        print(request.POST.get(Shoppinglist))
    return redirect("home")