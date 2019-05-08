from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ContactForm(forms.Form):
    To = forms.CharField()
    cc = forms.CharField(max_length=100)
    bcc = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=300)
    message = forms.CharField(widget=forms.Textarea)

