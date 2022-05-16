import attrs
from django import forms

class ContentInputForm(forms.Form):
    text = forms.CharField(max_length=10000000,
                            widget=forms.widgets.Textarea(
                            attrs={'class':'',
                                'cols':'60',
                                'rows':'10'}),
                            label="")
    