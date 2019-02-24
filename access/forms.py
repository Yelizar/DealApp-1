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

    def clean_user_type(self):
        user_type = self.cleaned_data.get("user_type")
        if not user_type:
            raise forms.ValidationError("You didn't choose user type!")
        return user_type

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    class Meta:
        model = UserProfile
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if not username:
            raise forms.ValidationError("Please insert your user name")
        try:
            user = UserProfile.objects.get(username=username)
            if user.password != password:
                raise forms.ValidationError("Invalid user credential")
        except UserProfile.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return username

