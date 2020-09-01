from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    # defaultis required=true, if not comp make it =False

    class Meta:
        # meta gives us nested namespace for configurations and keeps the config in 1 place 
        # and within the config we say that the model that would be affected wuld be user model
        # so when we do form.save it would save to user model
        model= User
        # it will be in the order as specified in the list
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['image']
