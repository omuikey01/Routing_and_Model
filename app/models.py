from django.db import models

# Create your models here.

class IndexForm(models.Model):
    person_name = models.CharField(max_length=50)
    person_email = models.EmailField(max_length=254)
