from product.models import ColorModel
from django import forms


class ColorModelForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = ColorModel
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }
