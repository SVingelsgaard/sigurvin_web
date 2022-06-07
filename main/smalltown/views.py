from django.shortcuts import render
from .models import Shoppinglist

#hompage
def home(request):
    if request.method == "POST":
        grocery = request.POST.get("grocery")
        Shoppinglist.objects.create(grocery = grocery, description = "blanch")

    return render(request, "smalltown.html", {"Shoppinglist": Shoppinglist.objects.all})