from django.db import models

# Create your models here.

class Guess(models.Model):
	guess = models.CharField(max_length=12, unique=True, blank=False)
	
	def __unicode__(self):
		return self.guess
