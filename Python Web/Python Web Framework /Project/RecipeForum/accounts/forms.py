from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class ProfileForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 8   }))
    class Meta:
        model = UserProfile
        exclude = ('user',)
        # widgets = {
        #     'info': Textarea(attrs={'cols': 80, 'rows': 5}),
        # }