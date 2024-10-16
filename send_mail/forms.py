from django import forms

class SendForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    content = forms.CharField(label="Content", max_length=200)