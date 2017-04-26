from django import forms

# forms.ModelForm to interact with model

class AuthForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=50)

class HouseSignupForm(AuthForm):
    # default widget should be text input
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput)
    repeat_password = forms.CharField(label='Repeat Password', max_length=50)
    remember_password = forms.BooleanField(label='Remember Password', required=False)
    field_order = ['username', 'email']

class SearchForm(forms.Form):
    location = forms.CharField(label='Location', max_length=100, required=False)
    max_price = forms.IntegerField(label='Max Price', required=False)
    field_order = ['max_price', 'location']
