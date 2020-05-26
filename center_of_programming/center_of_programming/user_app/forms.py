from django import forms


class html(forms.Form):
    first_name=forms.CharField(required=True)
    second_name = forms.CharField(required=True)
    third_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    mobile=forms.IntegerField(required=True)