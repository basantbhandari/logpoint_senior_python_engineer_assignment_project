from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
    password1 = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        labels = {'username': 'Username', 'email': 'Email', 'password1': 'Password', 'password2': 'Confirm Password'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                     'email': forms.EmailInput(attrs={'class': 'form-control'}),
                        'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                        'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                        }
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Your email is already in our list of users to be notified.Try a new email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ('username', 'password', )
        labels = {'username': 'Username', 'password': 'Password'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
                     'password': forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': True}),
                        }


                