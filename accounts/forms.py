from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
from django.contrib.auth.password_validation import validate_password


class SignUpForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('email', 'username','password')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):

    username = forms.EmailField(label = 'email')
    password = forms.CharField(label = 'パスワード',widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    username = forms.CharField(label = '名前')
    email = forms.EmailField(label = 'メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())


    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが違います')

    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password


    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
