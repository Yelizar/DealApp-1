from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['user_type', 'username', 'email']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user
#
# class FrameSignUpForm(Form):
#
#     username = CharField(max_length=128, min_length=4, widget=TextInput(attrs={'type': 'username'}))
#     password1 = CharField(widget=PadsswordInput(render_value=True))
#     password2 = CharField(widget=PasswordInput(render_value=True))
#     email = EmailField(widget=TextInput(attrs={'type': 'email'}))
#
#     CHOICES = [('buyer', 'buyer'),
#                ('supplier', 'supplier')]
#
#     like = ChoiceField(choices=CHOICES, widget=RadioSelect())
#
#     def __init__(self, *args, **kwargs):
#         super(FrameSignUpForm, self).__init__(*args, **kwargs)
#
#     def clean_username(self):
#         data = self.cleaned_data['username']
#         return data
#
#     def clean_email(self):
#         data = self.cleaned_data['email']
#         return data
#
#     def clear_like(self):
#         data = self.cleaned_data['like']
#         return data
#
#     def check_box(self):
#         if self.is_buyer and self.is_supplier:
#             self.add_error('username', 'Sorry problem on the server')
#
#     def clean(self):
#         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#             self.add_error('password1', 'Incorrect password')
#         return self.cleaned_data
#
#     def clean_password1(self):
#         data = self.cleaned_data['password1']
#         return data
#
#     def clean_password2(self):
#         data = self.cleaned_data['password2']
#         return data
#
#     def save(self):
#         data = self.cleaned_data
#         print(data['like'])
#
#         user = User.objects.create_user(username=data['username'], password=data['password1'],
#                                             email=data['email'], is_buyer=data['like'], is_supplier=data['like'])
#         user.save()