from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment

class RegisterForm(UserCreationForm):
    username = forms.CharField(label= "Никнейм", required= True, widget=forms.TextInput(attrs = {'class':'form-control mb-20'}))
    password1 = forms.CharField(label= "Пароль", required= True, widget=forms.PasswordInput(attrs = {'class':'form-control mb-20'}))
    password2 = forms.CharField(label= "Повторите пароль", required= True, widget=forms.PasswordInput(attrs = {'class':'form-control mb-20'}))
    email = forms.EmailField(label= "Почта", required= True, widget=forms.TextInput(attrs = {'class':'form-control mb-20'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]

        if commit:
            user.save()
            return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'input is-medium'}), required=True)

    class Meta:
        model = Comment
        fields = ('body',)