from django import forms

from .models import UserProfile


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


# class LogInForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label='Password')
#
#     class Meta:
#         model = UserProfile
#         fields = ['username']
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         return password

