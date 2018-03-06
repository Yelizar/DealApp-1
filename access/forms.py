from django.forms import *


class FrameSignUpForm(Form):

    username = CharField(max_length=128, min_length=4, widget=TextInput(attrs={'type': 'username'}))
    password1 = CharField(widget=PasswordInput(render_value=True))
    password2 = CharField(widget=PasswordInput(render_value=True))
    email = EmailField(widget=TextInput(attrs={'type': 'email'}))

    is_buyer = BooleanField(widget=(CheckboxInput({'type': 'is_buyer'})))
    is_supplier = BooleanField(widget=(CheckboxInput({'type': 'is_buyer'})))

    def __init__(self, *args, **kwargs):
        super(FrameSignUpForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def check_box(self):
        if self.is_buyer and self.is_supplier:
            self.add_error('username', 'Sorry problem on the server')


class SignUpForm(FrameSignUpForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', 'Incorrect password')
        return self.cleaned_data

