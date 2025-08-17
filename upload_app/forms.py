from django import forms
from main.models import *


class ResidenceForm(forms.ModelForm):
    class Meta:
        model = Residence
        fields = ['name', 'address', 'balance']  # Include fields you want in the form

        # Add widgets to customize the form's appearance
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter residence name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'balance': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Optional description'}),
        }


class PropriéterForm(forms.ModelForm):
    class Meta:
        model  = Propriéter
        
        fields = ["adress","propriéter_type", "residence", "description"]
        exclude = ["propriétaire"]
        widgets = {
            'adress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter residence adress'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter residence name'}),
            'propriéter_type': forms.Select(choices= (("propriéter","Propriéter") ,("loyer","Loyer")),attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'propriétaire': forms.TextInput(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'residence': forms.TextInput(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Optional description'}),
        }