from django.forms import ModelForm
from .models import Category

class Category_Form(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        # we can customize our fields like below
        #fields=['id','username','age',....'n']