from django import forms
from ext.models import Pdf

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = 'content',
