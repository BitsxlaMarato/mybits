from django.core.urlresolvers import reverse
from app.mixins import TabsViewMixin
from baggage.tables import BaggageListTable, BaggageListFilter
from baggage.models import Bag
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

def organizer_tabs(user):
    t = [('List', reverse('baggage_list'), False)]
    return t

class BaggageList(TabsViewMixin, SingleTableMixin, FilterView):
    template_name = 'baggage_list.html'
    table_class = BaggageListTable
    filterset_class = BaggageListFilter
    table_pagination = {'per_page': 100}
  
    def get_current_tabs(self):
        return organizer_tabs(self.request.user)
    
    def get_queryset(self):
        return Bag.objects.filter(active=True)