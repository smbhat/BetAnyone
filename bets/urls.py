from django.conf.urls import patterns, url
from bets import views

urlpatterns = patterns('', 
	# main view
	url(r'^$', views.index, name = 'index'),

	# dashboard view
	url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
	url(r'^betpage/(?P<cbet>[0-9]+)/$', views.betpage, name = 'betpage'),
	url(r'^deletebet/(?P<cbet>[0-9]+)/$', views.deletebet, name = 'deletebet'),
	url(r'^deleteuser/(?P<cfriend>[A-Za-z0-9]+)/$', views.deletefriend, name = 'deletefriend'),
	url(r'^addbet/(?P<cbet>[0-9]+)/$', views.addbet, name = 'addbet'),
	url(r'^ncommerce/$', views.ncommerce, name = 'ncommerce'),
	url(r'^betpagencommerce/$', views.betpagencommerce, name = 'betpagencommerce'),
	url(r'^search/$', views.search),
	url(r'^arbirate/(?P<cbet>[0-9]+)/$', views.arbitrate, name = 'arbitrate'),
	url(r'^arbitratedbet/(?P<cbet>[0-9]+)/$', views.arbitratedbet, name = 'arbitratedbet')

	)