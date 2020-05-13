from django import forms

#models
from .models import Subscribers

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...'
                }
            ),
        }