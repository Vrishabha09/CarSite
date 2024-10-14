from django import forms
from .models import bookSlot

class SlotForm(forms.ModelForm):
    class Meta:
        model = bookSlot
        fields = ['name','TimeSlot','Date','c_Name','email']