from django.conf.urls import patterns, include, url
from .views import DatasourcesView, MotivationtermAddView, MotivationtermDeleteView

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w,-]+)/data$', DatasourcesView.as_view(), name='DatasourcesView-data'),
)

management_urlpatterns = patterns('',
    url(r'^(?P<connector_slug>[\w,-]+)/motivationterm/add/',
	MotivationtermAddView.as_view(), name='motivationterm-add'),
    url(r'^(?P<connector_slug>[\w,-]+)/motivationterm/(?P<pk>[\w,-]+)/delete/',
	MotivationtermDeleteView.as_view(), name='motivationterm-delete'),
)
