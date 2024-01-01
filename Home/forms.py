from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput, ModelForm
from .models import UserData



class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        
        widgets = {
            "first_name":TextInput(attrs={"class":"form-control  py-3","placeholder":"First Name"}),
            "username":TextInput(attrs={"class":"form-control  py-3","placeholder":"Username"}), 
            "email":TextInput(attrs={"class":"form-control  py-3","placeholder":"Email Id"}),    
        }  
        
        def __init__(self, *args, **kwargs):
            super(UserAddForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control py-3', 'placeholder': 'Password'})
            self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control py-3', 'placeholder': 'Password confirmation'})

class UserDetailsForm(ModelForm):
    class Meta:
        model = UserData
        fields = ["name","house","phone","city","state"]