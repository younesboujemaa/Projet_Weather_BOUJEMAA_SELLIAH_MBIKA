# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SignupForm(UserCreationForm):

    username_regex = RegexValidator (regex =r'^[a-zA-Z0-9]*$', message = 'Votre nom d’utilisateur est incorrect')
    username = forms.CharField(validators=[username_regex], max_length=30,label='Nom d’utilisateur')


    nom_regex = RegexValidator (regex =r'^[a-zA-Z]*$', message = 'Votre nom est incorrect')
    Nom = forms.CharField(validators=[nom_regex], max_length=63, required= False )

    prenom_regex = RegexValidator (regex =r'^[a-zA-Z]*$', message = 'Votre prénom est incorrect')
    Prénom = forms.CharField(validators=[prenom_regex], max_length=63, required= False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Le numéro de téléphone doit être entrer dans un format différent.")
    Telephone = forms.CharField(validators=[phone_regex], max_length=17,required=False)


    dateNaissance = forms.DateField(label ='Date de Naissance', required= False)
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','Nom','Prénom','dateNaissance','Telephone')
        


# Pas de class Optionnal comme sur Java : le seul moyen c'est de mettre : required = false qui fait office ici d'optionnal