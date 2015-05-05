from django import forms
from bets.models import User, Bet

class CreateBetForm(forms.Form):
	amount = forms.FloatField(required = True, default = 0)

	def clean(self):
		cleaned_data = super(CreateBetForm, self).clean()
		a1 = cleaned_data.get("amount")