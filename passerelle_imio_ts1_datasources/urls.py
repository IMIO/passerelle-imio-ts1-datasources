from django.conf.urls import patterns, include, url
from .views import DatasourcesView, MotivationtermAddView

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w,-]+)/data$', DatasourcesView.as_view(), name='DatasourcesView-data'),
)

management_urlpatterns = patterns('',
    url(r'^(?P<connector_slug>[\w,-]+)/motivationterm/add/',
	MotivationtermAddView.as_view(), name='motivationterm-add'),
)
