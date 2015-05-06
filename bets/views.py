from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from bets.models import Bet, User

NETID = 'smbhat'

# Create your views here.
def index(request):
	return render(request, 'bets/index.html')

# Helper function to verify whether the input string represents a float. Return
# True if it does represent a float, False otherwise.
def verifiedNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def dashboard(request):
	u = User.objects.get(netid = NETID)


	if request.method == 'POST':
		if 'bet_name' in request.POST:
			n = request.POST['bet_name']
			amt = request.POST['bet_amt']
			d = request.POST['bet_desc']
			if verifiedNumber(amt):
				b = Bet(name = n, value = float(amt), description = d, category = '', creator = u)
				b.save()
				print 'New bet made.'
			else:
				print 'Not a valid amount.'

		elif 'netid' in request.POST:
			netid = request.POST['netid']
			if u.isFriend(netid) == False:
				u.addFriend(netid)
				u.save()
				print 'New friend added.'
			else:
				print 'Already friends.'
		
		elif 'card_amt' in request.POST:
			paymentamt = request.POST['card_amt']
			if verifiedNumber(paymentamt):
				u.addBalance(float(paymentamt))
				u.save()
				print 'New payment made.'
			else:
				print 'Not a valid amount.'

	balance = '$' + format(u.balance, '.2f')
	committed = '$' + format(u.committed, '.2f')
	availablefunds = '$' + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	allbets = Bet.objects.filter(creator = u)

	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

def betpage(request, cbet):


	bet = Bet.objects.get(id = cbet)
	arbitrator = 'Not Yet Taken'
	taker = 'Not Yet Taken'
	if bet.status == True:
		arbitrator = bet.arbitrator.netid
		taker = bet.taker.netid


	context = {'title': bet.name, 'description': bet.description, 'value': bet.value, 'creator': bet.creator.netid, 'arbitrator': arbitrator, 'taker': taker}

	return render(request, 'bets/betpage.html', context)