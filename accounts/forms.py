from django import forms

from django.contrib.auth import (

    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            # user_qs = User.objects.filter(username=username)
            # if user_qs.count() ==1:
            #     user = user_qs.first()
            if not user:
                raise forms.ValidationError("This user is not authenticated")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(label="Email Address" ,widget=forms.EmailInput)
    email2 = forms.CharField(label="Confirm Email" ,widget=forms.EmailInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")

        if email != email2:
            raise forms.ValidationError("email not matched")

        email_qs = User.objects.filter(email= email)
        if email_qs.exists():
            raise forms.ValidationError("the email has been registered")

        return email















