from django import forms
from .models import Transaction
from .models import Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'item_name', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'eco_friendly']
