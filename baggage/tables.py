import django_filters
import django_tables2 as tables
from baggage.models import Bag
from django.db.models import Q

class BaggageListFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search')

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(owner__email__icontains=value) | Q(owner__name__icontains=value))

    class Meta:
        model = Bag
        fields = ['search']

class BaggageListTable(tables.Table):

    class Meta:
        model = Bag
        attrs = {'class': 'table table-hover'}
        template = 'django_tables2/bootstrap-responsive.html'
        fields = ['owner', 'type', 'description', 'special']
        empty_text = 'No baggage items checked-in'