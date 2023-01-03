from django import forms

class CreateNewRecipe(forms.Form):
    name = forms.CharField(label='Name', max_length=100)