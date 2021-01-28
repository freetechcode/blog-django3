from django import forms


class SharingByEmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)

