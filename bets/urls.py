from django.conf.urls import patterns, url
from bets import views

urlpatterns = patterns('', 
	# main view
	url(r'^$', views.index, name = 'index'),

	)