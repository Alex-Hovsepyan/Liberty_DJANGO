from django import forms
from .models import CreatePost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateModelForm(forms.ModelForm):

    class Meta:

        model = CreatePost
        fields = ['user_title', 'user_description', 'user_name', 'user_price', 'user_royalty']



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user