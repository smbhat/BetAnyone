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

	u = get_object_or_404(Player, netid = request.user.username)


	if request.method == 'POST':
		if 'bet_name' in request.POST:
			n = request.POST['bet_name']
			amt = request.POST['bet_amt']
			desc = request.POST['bet_desc']
			c = request.POST['bet_challenge']
			date = request.POST['exp_date']
			arb = request.POST['bet_arbitrate']

			# if challenger field is filled out
			if c != '':
				try:
					challenged = get_object_or_404(Player, netid=c)
					arbitrator = get_object_or_404(Player, netid=arb)
					if verifiedNumber(amt):
						b = Bet(name = n, value = float(amt), description = desc, category = '', creator = u, taker = challenged, arbitrator = arbitrator, expdate = date)
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

	balance = u"\u00A3 " + format(u.balance, '.2f')
	committed = u"\u00A3 " + format(u.committed, '.2f')
	availablefunds = u"\u00A3 " + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	betscreated = Bet.objects.filter(creator = u)
	betstaken = Bet.objects.filter(taker = u)
	betsarbitrated = Bet.objects.filter(arbitrator = u)

	allbets = list(chain(betscreated, betstaken, betsarbitrated))
	engagedbets = list(chain(betscreated, betstaken))

	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(engagedbets)}
	return render(request, 'bets/dashboard.html', context)

@login_required
def betpage(request, cbet):

	bet = get_object_or_404(Bet, id = cbet)

	try:
		a = bet.arbitrator
		arbitrator = a.netid
	except ObjectDoesNotExist:
		arbitrator = 'Not Yet Taken'

	try:
		t = bet.taker
		taker = t.netid
	except ObjectDoesNotExist:
		taker = 'Not Yet Taken'



	context = {'title': bet.name, 'netid': request.user.username, 'description': bet.description, 'value': bet.value, 'creator': bet.creator.netid, 'arbitrator': arbitrator, 'taker': taker, 'betid': cbet, 'status': bet.status, 'expirydate': bet.expdate}

	return render(request, 'bets/betpage.html', context)

@login_required
# You add a bet if you've been invited to the bet as a taker.
def addbet(request, cbet):
	bet = get_object_or_404(Bet, id = cbet)
	u = get_object_or_404(Player, netid = request.user.username)

	bet.status = True
	bet.save()

	# commit money of both parties
	u.commitMoney(bet.value)
	c = bet.creator
	c.commitMoney(bet.value)

	u.save()
	c.save()

	print 'Bet accepted: ',
	print bet

	balance = u"\u00A3 " + format(u.balance, '.2f')
	committed = u"\u00A3 " + format(u.committed, '.2f')
	availablefunds = u"\u00A3 " + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	allfriends = u.friendlist.split('%') # list of friends

	betscreated = Bet.objects.filter(creator = u)
	betstaken = Bet.objects.filter(taker = u)
	betsarbitrated = Bet.objects.filter(arbitrator = u)

	print betstaken
	allbets = list(chain(betscreated, betstaken, betsarbitrated))
	
	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

def arbitrate(request, cbet):
	pass

@login_required
def deletebet(request, cbet):

	bet = get_object_or_404(Bet, id = cbet)
	bet.delete()
	print "Successfully deleted bet: ",
	print bet

	u = get_object_or_404(Player, netid = request.user.username)

	balance = u"\u00A3 " + format(u.balance, '.2f')
	committed = u"\u00A3 " + format(u.committed, '.2f')
	availablefunds = u"\u00A3 " + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	betscreated = Bet.objects.filter(creator = u)
	betstaken = Bet.objects.filter(taker = u)
	betsarbitrated = Bet.objects.filter(arbitrator = u)
	allbets = list(chain(betscreated, betstaken, betsarbitrated))
	
	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

@login_required
def deletefriend(request, cfriend):
	u = get_object_or_404(Player, netid = request.user.username)

	allfriends = u.friendlist.split('%')

	newlist = []

	for f in allfriends:
		if f != cfriend:
			newlist.append(f)

	u.friendlist = '%'.join(newlist)
	u.save()

	balance = u"\u00A3 " + format(u.balance, '.2f')
	committed = u"\u00A3 " + format(u.committed, '.2f')
	availablefunds = u"\u00A3 " + format(u.balance - u.committed, '.2f')

	allfriends = u.friendlist.split('%') # list of friends

	betscreated = Bet.objects.filter(creator = u)
	betstaken = Bet.objects.filter(taker = u)
	betsarbitrated = Bet.objects.filter(arbitrator = u)
	allbets = list(chain(betscreated, betstaken, betsarbitrated))
	
	context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
	return render(request, 'bets/dashboard.html', context)

@login_required
def arbitratedbet(request, cbet):

	bet = get_object_or_404(Bet, id = cbet)

	if request.method == 'POST':
		if 'taker' in request.POST:
			winnerid = bet.taker.netid
			loserid = bet.creator.netid
		else:
			winnerid = bet.creator.netid
			loserid = bet.taker.netid
		
		winner = get_object_or_404(Player, netid = winnerid)
		loser = get_object_or_404(Player, netid = loserid)

		winner.addBalance(2 * bet.value)
		winner.committed -= bet.value
		loser.committed -= bet.value

		winner.save()
		loser.save()

		bet.delete()

		u = get_object_or_404(Player, netid = request.user.username)

		balance = u"\u00A3 " + format(u.balance, '.2f')
		committed = u"\u00A3 " + format(u.committed, '.2f')
		availablefunds = u"\u00A3 " + format(u.balance - u.committed, '.2f')

		allfriends = u.friendlist.split('%') # list of friends

		betscreated = Bet.objects.filter(creator = u)
		betstaken = Bet.objects.filter(taker = u)
		betsarbitrated = Bet.objects.filter(arbitrator = u)

		allbets = list(chain(betscreated, betstaken, betsarbitrated))

		context = {'netid': u.netid, 'betlist': allbets, 'friendslist': allfriends, 'balance': balance, 'committed': committed, 'availablefunds': availablefunds, 'numfriends': len(allfriends), 'numbets': len(allbets)}
		return render(request, 'bets/dashboard.html', context)

	else:
		arbitrator = 'Not Yet Taken'
		taker = 'Not Yet Taken'
		if bet.status == True:
			arbitrator = bet.arbitrator.netid
			taker = bet.taker.netid

		context = {'title': bet.name, 'netid': request.user.username, 'description': bet.description, 'value': bet.value, 'creator': bet.creator.netid, 'arbitrator': arbitrator, 'taker': taker, 'betid': cbet}
		return render(request, 'bets/betpage.html', context)
			

@login_required
def search(request):
	print '---Search Request---'
	print request.GET
	print request.GET['q']

	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']

		print q

		betlist = Bet.objects.filter(name__icontains = q)
		context = {'betlist': betlist, 'searchquery': q}

		return render(request, 'bets/searchresults.html', context)
	return HttpResponse(message)

# STATIONARY PAGES
@login_required
def ncommerce(request):
	return render(request, 'bets/ncommerce.html')

@login_required
def betpagencommerce(request):
	return render(request, 'bets/betpagencommerce.html')



