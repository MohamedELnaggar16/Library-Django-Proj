from django import forms
from .models import Book , Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = '__all__'
        
        widgets = {
        'title': forms.TextInput(attrs={'class':"form-control"}) ,
        'aurthor': forms.TextInput(attrs={'class':"form-control"}) ,
        'photo_book': forms.FileInput(attrs={'class':"form-control"}) ,
        'photo_author': forms.FileInput(attrs={'class':"form-control"}) ,
        'pages': forms.NumberInput(attrs={'class':"form-control"}) ,
        'price': forms.NumberInput(attrs={'class':"form-control"}) ,
        'rental_price_day': forms.NumberInput(attrs={'class':"form-control" , 'id':'rentalPriceDay'}) ,
        'rental_period': forms.NumberInput(attrs={'class':"form-control", 'id':'rentalPeriod'}) ,
        'total_rental' : forms.NumberInput(attrs={'class':"form-control", 'id':'totalRental'}) ,
        'status': forms.Select(attrs={'class':"form-control"}) ,
        'category': forms.Select(attrs={'class':"form-control"}) ,
        }
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
        widgets = {
        'name': forms.TextInput(attrs= {'class':'form-control'})
        
        }