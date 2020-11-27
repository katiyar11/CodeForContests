from django import forms
from .models import Contests
from datetime import datetime 
#DataFlair


class ContestCreate(forms.ModelForm):
    
    contest_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter the contest name'
        }))

    
    image= forms.ImageField(widget=forms.FileInput(
        attrs={
            'type':'file'
        }
    ))

    description =forms.CharField(widget=forms.TextInput(
        attrs={
            
            'class': 'form-control',
            'placeholder': 'Enter the description'
        }))


    input_format = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Input'
    }))

    output_format = forms.CharField(widget=forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Output'
    }))

    created = forms.DateField(widget=forms.DateInput(
    attrs={
    'class': 'form-control',
    'type':'date'
    # 'placeholder': 'Select start date'
    # 'value': datetime.now()
    }))

    class Meta:
        model=Contests
        fields =['contest_name','image','description','input_format','output_format','created'] 

        



    

    # Price =forms.IntegerField(widget=forms.NumberInput(
    #     attrs={ 
    #         'class': 'form-control',
    #         'placeholder': 'Enter the prize'
    #     }))


    # End_date=  forms.DateField( 
    #     widget=forms.DateInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'type':'date',
    #         'placeholder': 'Select start date'
    #     }))
    

    # Contest_Type = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter the contest name'
    #     }))