from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import ContactModel,PropertyListing



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class AddPropertyForm(ModelForm):
    class Meta:
        model = PropertyListing
        fields = '__all__'