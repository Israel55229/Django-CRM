from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Record
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<span class='form-text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small> </span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm  password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



#  Form for add Records
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'First Name',
                'required': 'True',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'Last Name',
                'required': 'True'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'Email Address',
                'required': 'True'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': '(+233) 456 7890 422',
                'required': 'True'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'Enter address',
                'required': 'True'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'Enter city',
                'required': 'True'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': 'Enter state',
                'required': 'True'
            }),
            'zipcode': forms.TextInput(attrs={
                'class': 'form-control fst-italic',
                'placeholder': '02231',
                'required': 'True'
            })
        }
        