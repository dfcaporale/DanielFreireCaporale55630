from django import forms

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

#class ArtistForm(forms.Form):
#    name = forms.CharField(max_length=50, required=True)
#    webpage = forms.CharField(max_length=50, required=True)

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=50, required=True)
    artist = forms.CharField(max_length=50, required=True)
    country = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    venue = forms.CharField(max_length=50, required=True)
    date = forms.DateField(required=True)
    # sold_out = forms.BooleanField()

class ClientForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

class VenueForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    country = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    address = forms.CharField(max_length=50, required=True)
    webpage = forms.URLField(required=True)

class ArtistForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    webpage = forms.URLField(required=True)

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=50, required=True)
    artist = forms.CharField(max_length=50, required=True)
    venue = forms.CharField(max_length=50, required=True)
    date = forms.DateField(required=True)
    soldOut = forms.BooleanField()

#________________________________________________________

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Client email")
    password1 = forms.CharField(label="Password", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Client email", required=True)
    #password1 = forms.CharField(label="Password", widget= forms.PasswordInput)
    #password2 = forms.CharField(label="Confirm password", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="First name", max_length=50, required=False)   
    last_name = forms.CharField(label="Last name", max_length=50, required=False)   

    class Meta:
        model = User
        #fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        fields = ['email', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

#________________________________________________________________
class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Current password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("New Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repeat New Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')