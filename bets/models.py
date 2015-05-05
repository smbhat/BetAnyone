from django.db import models

# Create your models here.
class User(models.Model):
	netid = models.CharField(max_length = 50)
	balance = models.FloatField(default = 0)
	committed = models.FloatField(default = 0)

	def getNetID(self):
		return self.netid

	# add amt to User's current balance
	def addBalance(self, amt):
		self.balance += amt

	# Move money (amt) from balance to committed. Return True if successful; 
	# return False if failed (insufficient funds)
	def commitMoney(self, amt):
		if amt > self.balance:
			return False
		else:
			self.balance -= amt
			self.committed += amt
			return True

	def __str__(self):
		return self.netid

class Bet(models.Model):
	name = models.CharField(max_length = 100, default='')
	description = models.CharField(max_length = 1000)
	value = models.IntegerField(default = 0)
	category = models.CharField(max_length = 50)
	status = models.BooleanField(default = False) # True if taken, False if open

	creator = models.ForeignKey(User, related_name = 'creator')
	taker = models.ForeignKey(User, related_name = 'taker', default = 0)
	arbitrator = models.ForeignKey(User, related_name = 'arbitrator', default = 0)

	def __str__(self):
		return self.name