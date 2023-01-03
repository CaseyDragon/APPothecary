from django.db import models

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