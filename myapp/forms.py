from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from myapp import models




class LoginForm(forms.Form):
    username = forms.CharField(
        label=("Username"),
        widget=forms.TextInput(
            attrs={"id": "login_username", "autocomplete": "new-username"}))

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',"id": "login_password"}),
    )


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="User name",
        help_text="Only letters can be entered! For login.",
        widget=forms.TextInput(attrs={"id": "register_username", "autocomplete": "new-username"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', "id": "register_password"}),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Enter the same password as before, for verification."
    )
    birthday = forms.DateField(
        label="Birthday",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = models.UserInfo
        fields = ("username", "nick_name", "gender", "email", "birthday", "password1", "password2", "birthday")
        exclude = ('avatar', 'signature', 'user')


    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1:
            password_validation.validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two passwords are inconsistent!",
                code='password_mismatch',
            )
        return password1

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError("Username already exists!")
        except User.DoesNotExist:
            return username


class UserProfileForm(forms.ModelForm):
    signature = forms.CharField(
        label="Signature",
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 15})
    )

    birthday = forms.DateField(
        label="Birthday",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = models.UserInfo
        exclude = ("user",)


class AddMessageForm(forms.ModelForm):
    user = forms.CharField(
        label="User",
        widget=forms.HiddenInput()
    )
    to_user = forms.CharField(
        label="To User",
        widget=forms.HiddenInput()
    )



    def clean_user(self):
        user = self.cleaned_data["user"]
        try:
            user = User.objects.get(id=user)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist!")

    def clean_to_user(self):
        to_user = self.cleaned_data["to_user"]
        try:
            user = User.objects.get(id=to_user)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist!")




