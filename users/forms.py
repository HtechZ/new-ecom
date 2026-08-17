from django import forms

class Form(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id":"form-username","class":"form-input form-input-required","placeholder":"Enter your Username"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"id":"form-phonenumber","class":"form-input form-input-required","placeholder":"Enter your Phone Number"}))
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={"id":"form-email","class":"form-input","placeholder":"Enter your Email"}))