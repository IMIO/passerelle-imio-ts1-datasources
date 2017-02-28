# from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView
from django.views.generic.detail import SingleObjectMixin

from .models import ImioTs1Datasources, MotivationTerm
from .forms import MotivationTermForm


class DatasourcesView(View, SingleObjectMixin):
    model = ImioTs1Datasources
    # form_class = DatasourcesForm


# DatasourcesAddView is missing a QuerySet. Define DatasourcesAddView.model,
# DatasourcesAddView.queryset, or override DatasourcesAddView.get_queryset().
class MotivationtermAddView(CreateView):
    model = MotivationTerm
    form_class = MotivationTermForm
    template_name = 'passerelle_imio_ts1_datasources/motivationterm_form.html'
