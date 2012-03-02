from django import forms
from main.models import Zombie
from main.models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet


class ZombieForm(forms.ModelForm):
    class Meta:
        model = Zombie