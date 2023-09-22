from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(label='Nome',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class': 'form-control'}))