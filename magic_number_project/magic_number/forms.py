from django import forms
from django.template.defaultfilters import mark_safe
from captcha.fields import CaptchaField
from magic_number.models import Guess


class GuessForm(forms.ModelForm):
	guess = forms.CharField(label=mark_safe("<h1>Guess the Magic Word</h1>"),
							widget=forms.TextInput(attrs={'class' : 'form-control guess'}),
							max_length=12,
							error_messages={'required' : "You cannot guess blank. Blank isnt even a word.", 
											'max_length' : "You guessed a word that is too big.",
											'unique' : 'unique_error'},)
											
	captcha = CaptchaField(error_messages={'required' : "You didn't type anything in the captcha.",
											'invalid':"That is not the correct captcha."})
											
	
	class Meta:
		model = Guess
		fields = ('guess', 'captcha')
