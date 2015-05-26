import random 
from magic_number.models import Guess

def gen():
	
	guesses = Guess.objects.all()
	captcha_text = str(guesses[random.randint(0,guesses.count() - 1 )])[::-1]
	
	return (captcha_text, captcha_text)
