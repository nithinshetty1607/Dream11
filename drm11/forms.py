from django import forms



class PredForm(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Email = forms.CharField(label='Email', max_length=100)
    PlayerName=forms.CharField(label='PlayerName', max_length=100)