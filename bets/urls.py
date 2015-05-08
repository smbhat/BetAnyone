from django.conf.urls import patterns, url
from bets import views

urlpatterns = patterns('', 
	# main view
	url(r'^$', views.index, name = 'index'),

	# dashboard view
	url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
	url(r'^betpage/(?P<cbet>[0-9]+)/$', views.betpage, name = 'betpage'),
	url(r'^deletebet/(?P<cbet>[0-9]+)/$', views.deletebet, name = 'deletebet'),
	url(r'^deleteuser/(?P<cfriend>[A-Za-z]+)/$', views.deletefriend, name = 'deletefriend'),
	url(r'^addbet/(?P<cbet>[0-9]+)/$', views.addbet, name = 'addbet'),
	url(r'^ncommerce/$', views.ncommerce, name = 'ncommerce'),
	)