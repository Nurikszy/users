from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = ((ADMIN, "ADMIN"), (VIPClient, "VIP-Client"), (CLIENT, "CLIENT"))
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = ((MALE, "MALE"), (FEMALE, "FEMALE"), (OTHER, "OTHER"))


BISHKEK = 1
OSH = 2
TALAS = 3
Issyk_Kul = 4
NARYN = 5
JALAL_ABAD = 6
BATKEN = 7
region = (
    (BISHKEK, "BISHKEK"),
    (OSH, "OSH"),
    (TALAS, "TALAS"),
    (Issyk_Kul, "ISSYK KUL"),
    (NARYN, "NARYN"),
    (JALAL_ABAD, "JALAL ABAD"),
    (BATKEN, "BATKEN"),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    culepassword = forms.CharField(max_length=90)
    region = forms.ChoiceField(choices=region, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
            "culepassword",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username", "id": "hello"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password",
                "id": "hi",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "email": "from-control",
                "placeholder": "введите почту..",
                "id": "sup",
            }
        )
    )
