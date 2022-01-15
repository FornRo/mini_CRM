from django_filters import FilterSet, ChoiceFilter
from .models import Company

__all__ = [
    'CompanyFilter',
]


class CompanyFilter(FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    )
    name_company = ChoiceFilter(label='Name_company', choices=CHOICES, method='filter_by_order')
    name = ChoiceFilter(label='Name', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Company
        fields = {
        }

    def filter_by_order(self, qs, name, val):
        expression = f'{name}' if val == 'ascending' else f'-{name}'
        return qs.order_by(expression)
