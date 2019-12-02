from django import forms
from apps.hotel.models import Motel


class hotelForm(forms.ModelForm):
    
    class Meta:

        model = Motel

        fields = (
            'nombre',
            'apellido',
            'correo',
            'fecha',
        ) 
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo electronico',
            'fecha': 'Fecha de nacimiento',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
        }