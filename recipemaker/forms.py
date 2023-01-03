from django import forms

class CreateNewRecipe(forms.Form):
    name = forms.CharField(max_length=100)
    superfat = forms.IntegerField()
    lyetype = forms.CharField(max_length= 10)
    lyeamount = forms.DecimalField(max_digits=6, decimal_places=2)
    lyeadditives = forms.CharField(max_length=100)
    oilname = forms.CharField(max_length=100)
    oilamount = forms.DecimalField(max_digits=6, decimal_places=2)
    additive = forms.CharField(max_length=100)