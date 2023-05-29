from django import forms
from . import models

class ClothitemForm(forms.ModelForm):
    class Meta:
        model = models.Clothingitem
        fields = "__all__"
        #fields = "title description image"
