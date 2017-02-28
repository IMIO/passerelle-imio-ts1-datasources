# passerelle-imio-ts1-datasources - passerelle connector to ts1 datasources import and manage
# Copyright (C) 2016  Entr'ouvert
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils.translation import ugettext_lazy as _

from passerelle.base.models import BaseResource
from passerelle.utils.api import endpoint


class MotivationTerm(models.Model):
    text = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ['text']

    def save(self, *args, **kwargs):
        return super(MotivationTerm, self).save(*args, **kwargs)


class ImioTs1Datasources(BaseResource):

    lst_motivations_terms = [{'text': u'mon motif', 'price': 0.0, 'id': 'mon-motif', 'description': u''},
                         {'text': u"Allocations d'\xe9tudes", 'price': 3.0, 'id': 'allocations-detudes', 'description': u'<p>Bla Bla</p>'},
                         {'text': u'Cr\xe8che : gratuit', 'price': 0.0, 'id': 'creche', 'description': u'Cr\xe8che'},
                         {'text': u'Consulat : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'consulat', 'description': u'Consulat'},
                         {'text': u"Bourse d'\xe9tudes : gratuit", 'price': 0.0, 'id': 'bourse-d-etudes', 'description': u"Bourse d'\xe9tudes"},
                         {'text': u'Banque : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'banque', 'description': u'Banque'},
                         {'text': u'Avocat : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'avocat', 'description': u'Avocat'},
                         {'text': u'Autre : indiquer la raison dans le commentaire', 'price': 0.0, 'id': 'autre', 'description': u'Autre'},
                         {'text': u'Assurance : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'assurance', 'description': u'Assurance'},
                         {'text': u'Allocations familiales : gratuit', 'price': 0.0, 'id': 'allocations-familiales', 'description': u'Allocations familiales'},
                         {'text': u"Usage \xe0 l'\xe9tranger : co\xfbt 2\u20ac", 'price': 2.0, 'id': 'usage-etranger', 'description': u"Usage \xe0 l'\xe9tranger"},
                         {'text': u'Syndicat - ONEM : gratuit', 'price': 0.0, 'id': 'syndicat', 'description': u'Syndicat'},
                         {'text': u'Succession : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'succession', 'description': u'Succession'},
                         {'text': u'R\xe9gion Wallonne : gratuit', 'price': 0.0, 'id': 'region-wallonne', 'description': u'R\xe9gion Wallonne'},
                         {'text': u'Pour mariage en Belgique : gratuit', 'price': 0.0, 'id': 'pour-mariage-belgique', 'description': u'Pour mariage en Belgique'},
                         {'text': u'Pension : gratuit', 'price': 0.0, 'id': 'pension', 'description': u'Pension'},
                         {'text': u'Notaire : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'notaire', 'description': u'Notaire'},
                         {'text': u'Mutuelle : gratuit', 'price': 0.0, 'id': 'mutuelle', 'description': u'Mutuelle'},
                         {'text': u'Logement social : gratuit', 'price': 0.0, 'id': 'logement-social', 'description': u'Logement social'},
                         {'text': u'Huissier : co\xfbt 2\u20ac', 'price': 2.0, 'id': 'huissier', 'description': u'Huissier'},
                         {'text': u'Ecole : gratuit', 'price': 0.0, 'id': 'ecole', 'description': u'Ecole'},
                         {'text': u"Demande d'emploi : gratuit", 'price': 0.0, 'id': 'demande-d-emploi', 'description': u"Demande d'emploi"}
                         ]

    category = _('Datasources manager')

    class Meta:
        verbose_name = _('TS1 datasources manage Service')


    @classmethod
    def get_verbose_name(cls):
        return cls._meta.verbose_name

    @classmethod
    def get_icon_class(cls):
        return ''

    @classmethod
    def get_connector_slug(cls):
        return 'imio-ts1-datasources'

    def get_motivation_terms(self):
        return MotivationTerm.objects.all()

    @endpoint()
    def motivationterms(self, request, **kwargs):
        motivation_terms = []
        for motivation in self.get_motivation_terms():
            motivation_terms.append({"id": motivation.id,
                                     "text": motivation.text,
                                     "price": str(motivation.price)})
        return {"data": motivation_terms}
