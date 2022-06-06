from django.db import models

class Shoppinglist(models.Model):
    grocery = models.CharField(max_length=255)
    description = models.TextField(default="description")


    def __str__(self):
	    return self.grocery