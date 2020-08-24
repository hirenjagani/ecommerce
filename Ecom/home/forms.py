from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()

class Contact(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    content=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"write description"}))

    def clean_email(self):
        email=self.cleaned_data.get("email")
        # if not "@gmail.com" in email:
        #     raise forms.ValidationError("please write gmail.com")
        # return email

class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())




class Register(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
          raise forms.ValidationError("This usename is already taken")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
          raise forms.ValidationError("This email is already exist")
        return email

    def clean(self):
        data=self.cleaned_data
        pass1=self.cleaned_data.get("password1")
        pass2=self.cleaned_data.get("password2")

        if pass1 != pass2:
            raise forms.ValidationError("password must not match")
        return data