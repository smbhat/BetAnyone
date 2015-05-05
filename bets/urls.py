from django.conf.urls import patterns, url
from bets import views

urlpatterns = patterns('', 
	# main view
	url(r'^$', views.index, name = 'index'),

	# dashboard view
	url(r'^dashboard/$', views.dashboard, name = 'dashboard')

	)