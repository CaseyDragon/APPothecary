from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Oils(models.Model):
    name = models.CharField(max_length=100)
    k_sap = models.DecimalField(max_digits=5, decimal_places=4)
    na_sap = models.DecimalField(max_digits=5, decimal_places=4)
    hard = models.BooleanField()
    iodine = models.IntegerField()
    INS = models.IntegerField()
    lauric = models.IntegerField()
    myristic = models.IntegerField()
    palmitic = models.IntegerField()
    stearic = models.IntegerField()
    ricinoleic = models.IntegerField()
    oleic = models.IntegerField()
    linoleic = models.IntegerField()
    linolenic = models.IntegerField()
    suggested = models.CharField(max_length = 100)
    maxuse = models.CharField(max_length = 100)
    hardness = models.IntegerField()
    cleansing= models.IntegerField()
    moisturizing = models.IntegerField()
    bubbles = models.IntegerField()

    def __str__(self):
        return self.name


class Additives(models.Model):
    name = models.CharField(max_length=100)
    suggested = models.CharField(max_length = 100)
    maxuse = models.CharField(max_length = 100)
    lyephase = models.BooleanField()

    def __str__(self):
        return self.name

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes", null=True)
    name = models.CharField(max_length=100)
    superfat = models.IntegerField()
    lyetype = models.CharField(max_length= 10)
    lyeamount = models.DecimalField(max_digits=6, decimal_places=2)
    lyeadditives = models.CharField(max_length=100)
    oilname = models.CharField(max_length=100)
    oilamount = models.DecimalField(max_digits=6, decimal_places=2)
    additive = models.CharField(max_length=100)

    def __str__(self):
        return self.name


