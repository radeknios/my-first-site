from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Available

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # widget generuje element html <input> z atrybutem type = password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('date_of_birth', 'photo')

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'location')

class AddAvailable(forms.ModelForm):
    class Meta:
        model = Available
        fields = ('start', 'end')


