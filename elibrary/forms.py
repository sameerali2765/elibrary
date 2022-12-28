from django import forms

class ContactForm(forms.Form):

    message = forms.CharField(widget=forms.Textarea(
         attrs={'class': 'form-control w-100','placeholder':' Enter Message',}
         ))
    name = forms.CharField(widget=forms.TextInput( 
        attrs={'class': 'form-control','placeholder':' Enter Name',}
        ))
    email = forms.EmailField(widget=forms.TextInput(
         attrs={'class': 'form-control ','placeholder':' Enter Email',}
        ))
    subject = forms.CharField(widget=forms.TextInput( 
        attrs={'class': 'form-control','placeholder':' Enter Subject',}
        ))
