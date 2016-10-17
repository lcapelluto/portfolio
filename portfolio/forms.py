from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100)
    message = forms.CharField(required=True, max_length=2000, widget=forms.Textarea)