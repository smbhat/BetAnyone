from django.db import models

# Create your models here.
class User(models.Model):
	netid = models.CharField(max_length = 50)
	balance = models.FloatField(default = 0)
	committed = models.FloatField(default = 0)



class Bet(models.Model):
	description = models.CharField(max_length = 1000)
	value = models.IntegerField(default = 0)
	category = models.CharField(max_length = 50)
	status = models.BooleanField(default = False) # True if taken, False if open

	creater = models.ForeignKey(User)
	taker = models.ForeignKey(User)
	arbitrator = models.ForeignKey(User)