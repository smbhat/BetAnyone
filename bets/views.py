from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from bets.models import Bet, User



# Create your views here.
def index(request):
	return render(request, 'bets/index.html')