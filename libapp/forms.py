from django import forms
from .models import*

class Book_Signupform(forms.ModelForm):
    class Meta:
        db_table = Book_Signup
        fields ='__all__'

class Book_Storeform(forms.ModelForm):
    class Meta:
        db_table = Book_Store
        fields ='__all__'
        
        