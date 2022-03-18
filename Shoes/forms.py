from socket import fromshare
from django import forms 
from .models import Shoe, Product, Review 

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'