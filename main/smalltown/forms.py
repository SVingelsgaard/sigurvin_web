from dataclasses import fields
from django.forms import ModelForm

from .models import *

class ShoppinglistForm(ModelForm):
    class Meta:
        model = Shoppinglist
        fields = ["grocery", "description"]