from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from main_app.models import Meeting, Conclusion
from phonenumber_field.formfields import PhoneNumberField


class NewAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]
        labels = {"username": "Логин", "password": "Пароль"}


class NewConclusionCreate(forms.ModelForm):
    conclusion_desc = forms.TextInput
    class Meta:
        model = Conclusion
        fields = ["conclusion_desc"]


class NewUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username",
                  'first_name',
                  'last_name',
                  "email"]
        exclude = ["password1",
                   "password2",
                   "last_login",
                   "is_superuser",
                   "_groups",
                   "_user_permissions",
                   "is_staff",
                   "is_active",
                   'date_joined']
        labels = {
            "username": "Логин",
            'first_name': "Имя",
            'last_name':"Фамилия",
            "email":"Email"
        }


class MeetingCreateForm(forms.ModelForm):
    phone_number = PhoneNumberField(label="Номер телефона")
    description = forms.TextInput
    user = forms.IntegerField

    class Meta:
        model = Meeting
        fields = ["phone_number", "description"]
        labels = {
            'description': "Описание причины обращения",
        }

    def save(self, commit=True):
        meeting = super(MeetingCreateForm, self).save(commit=False)
        meeting.phone_number = self.cleaned_data["phone_number"]
        meeting.description = self.cleaned_data["description"]
        if commit:
            meeting.save()
        return meeting





class NewUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ["username",
                  "first_name",
                  "last_name",
                  'email',
                  'password1',
                  "password2"
        ]
        labels = {
            "username": "Логин",
            "password1": "Пароль",
            "password2": "Повторите пароль"
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

