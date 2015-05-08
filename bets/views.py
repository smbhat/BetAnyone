from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from bets.models import Bet, Player
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from itertools import chain

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

@login_required
def dashboard(request):
	print '----NETID----'
	print request.user.username
	print '----NETID----'

	u = get_object_or_404(Player, netid = request.user.username)


	if request.method == 'POST':
		if 'bet_name' in request.POST:
			n = request.POST['bet_name']
			amt = request.POST['bet_amt']
			desc = request.POST['bet_desc']
			c = request.POST['bet_challenge']
			date = request.POST['exp_date']

			# if challenger field is filled out
			if c != '':
				try:
					challenged = get_object_or_404(Player, netid=c)
					if verifiedNumber(amt):
						b = Bet(name = n, value = float(amt), description = desc, category = '', creator = u, taker = challenged, expdate = date)
						b.save()

				except ObjectDoesNotExist:
					print 'invalid netid'
			# if challenger field is left empty
			else:
				if verifiedNumber(amt):
					b = Bet(name = n, value = float(amt), description = desc, category = '', creator = u, expdate = date)
					b.save()
					print 'New bet made.'

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

	betscreated = Bet.objects.filter(creator = u)
	betstaken = Bet.objects.filter(taker = u)
	betsarbitrated = Bet.objects.filter(arbitrator = u)

	allbets = list(chain(betscreated, betstaken, betsarbitrated))

	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

@login_required
def betpage(request, cbet):


	bet = get_object_or_404(Bet, id = cbet)
	arbitrator = 'Not Yet Taken'
	taker = 'Not Yet Taken'
	if bet.status == True:
		arbitrator = bet.arbitrator.netid
		taker = bet.taker.netid


	context = {'title': bet.name, 'description': bet.description, 'value': bet.value, 'creator': bet.creator.netid, 'arbitrator': arbitrator, 'taker': taker}

	return render(request, 'bets/betpage.html', context)

@login_required
def deletebet(request, cbet):

	bet = get_object_or_404(Bet, id = cbet)
	bet.delete()
	print "Successfully deleted bet: ",
	print bet

	u = get_object_or_404(Player, netid = request.user.username)

	balance = '$' + format(u.balance, '.2f')
	committed = '$' + format(u.committed, '.2f')
	availablefunds = '$' + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	allbets = Bet.objects.filter(creator = u)

	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

def deletefriend(request, cfriend):
	u = get_object_or_404(Player, netid = request.user.username)

	allfriends = u.friendlist.split('%')

	newlist = []

	for f in allfriends:
		if f != cfriend:
			newlist.append(f)

	u.friendlist = '%'.join(newlist)
	u.save()

	balance = '$' + format(u.balance, '.2f')
	committed = '$' + format(u.committed, '.2f')
	availablefunds = '$' + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	allbets = Bet.objects.filter(creator = u)

	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)





