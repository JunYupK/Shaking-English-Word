from django import forms

class TextFrom(forms.Form):
    text_search = forms.CharField(label='Text Search', max_length=100)