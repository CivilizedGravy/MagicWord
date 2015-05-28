from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from magic_word.models import Guess
from magic_word.forms import GuessForm
import random
# Create your views here.

def index(request):
	context_dict = {}
	is_correct = None
	guess= ''
	errors = {}
	
	if request.method == 'POST':
		guessform = GuessForm(data=request.POST)
		guess = request.POST.get('guess')
		if guessform.is_valid():
			if guess.lower() == 'lotion':
				is_correct=True
			else:
				is_correct=False
				guessform.save(commit=True)
				
		elif 'unique_error' in guessform['guess'].errors:
			is_correct = False 
		
			
	else:
		guessform = GuessForm()
	
	
	context_dict = {'is_correct' : is_correct, 'guessform'  : guessform}
	return render(request, 'magic_word/index.html', context_dict)


def check(request):

	
	return HttpResponseRedirect('/')
	
