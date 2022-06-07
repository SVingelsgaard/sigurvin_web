from django.shortcuts import render
from .models import Shoppinglist

#hompage
def home(request):
    if request.method == "POST":
        grocery = request.POST.get("grocery")
        Shoppinglist.objects.create(grocery = grocery, description = "blanch")
        #shoud make it so i the item is not named shoppinglist

    return render(request, "smalltown.html", {"Shoppinglist": Shoppinglist.objects.all})