from django import forms

class PositionForm(forms.Form):
    postion = forms.CharField()