from django.forms import *
from django.contrib.auth.models import User
from .models import *


class FrameSignUpForm(Form):

    username = CharField(max_length=128, min_length=4, widget=TextInput(attrs={'type': 'username'}))
    password1 = CharField(widget=PasswordInput(render_value=True))
    password2 = CharField(widget=PasswordInput(render_value=True))
    email = EmailField(widget=TextInput(attrs={'type': 'email'}), disabled=True)

    is_buyer = BooleanField(widget=(CheckboxInput({'type': 'is_buyer'})))
    is_supplier = BooleanField(widget=(CheckboxInput({'type': 'is_supplier'})))

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

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', 'Incorrect password')
        return self.cleaned_data

    def clean_password1(self):
        data = self.cleaned_data['password1']
        return data

    def clean_password2(self):
        data = self.cleaned_data['password2']
        return data

    def clean_is_buyer(self):
        data = self.cleaned_data['is_buyer']
        return data

    def clean_is_supplier(self):
        data = self.cleaned_data['is_supplier']
        return data

    def save(self):
        data = self.cleaned_data
        # user = User.objects.create_user(username=data['username'], password=data['password1'],
        #                                 email=data['email'])
        form_user = UserProfile.objects.create_user(username=data['username'], password=data['password1'],
                                        email=data['email'], is_buyer=data['is_buyer'], is_supplier=data['is_supplier'])
        # user.save()
        form_user.save()


# class LogInForm(FrameSignUpForm):
#     def __init__(self, *args, **kwargs):
#         super(LogInForm, self).__init__(*args, **kwargs)


class FrameEmail(ModelForm):

    class Meta:
        model = EmailModel
        fields = '__all__'







