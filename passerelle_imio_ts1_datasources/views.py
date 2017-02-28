# from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse

from .models import ImioTs1Datasources, MotivationTerm


class DatasourcesView(View, SingleObjectMixin):
    model = ImioTs1Datasources
    # form_class = DatasourcesForm


# DatasourcesAddView is missing a QuerySet. Define DatasourcesAddView.model,
# DatasourcesAddView.queryset, or override DatasourcesAddView.get_queryset().
class MotivationtermAddView(CreateView):
    model = MotivationTerm
    fields = '__all__'
    template_name = 'passerelle_imio_ts1_datasources/motivationterm_form.html'

    def get_success_url(self):
        connector = ImioTs1Datasources.objects.get(slug=self.kwargs['connector_slug'])
        return reverse('view-connector',
                kwargs={'connector': connector.get_connector_slug(),
                        'slug': connector.slug})
