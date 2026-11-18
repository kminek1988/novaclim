from django import forms
from .models import ContactForm

class PostForm(forms.ModelForm):
    policy = forms.BooleanField(label='Akceptuję zasady polityki prywatności', required=True, widget=forms.CheckboxInput())
    
    class Meta:
        model = ContactForm
        fields = '__all__'

