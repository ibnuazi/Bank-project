from django import forms

class indexform(forms.Form):
    usname=forms.CharField(max_length=30)
    psw=forms.IntegerField()


class bankform(forms.Form):
    fname = forms.CharField(max_length=30)
    lname = forms.CharField(max_length=30)
    uname = forms.CharField(max_length=20)
    email = forms.EmailField()
    ph = forms.IntegerField()
    file = forms.FileField()
    pin = forms.IntegerField()
    repin = forms.IntegerField()

class notificationform(forms.Form):
    topic=forms.CharField()
    content=forms.CharField()

class adminform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class moneyform(forms.Form):
    name=forms.CharField(max_length=20)
    acc=forms.IntegerField()
    amount=forms.IntegerField()