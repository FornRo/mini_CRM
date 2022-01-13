from django_filters import FilterSet, MultipleChoiceFilter
from .models import Cooperation, CHANNEL, RATING

__all__ = [
    'CooperationFilterSet',
]

# CHOICES = (
#         ('ascending', 'Ascending'),
#         ('descending', 'Descending'),
#     )


class CooperationFilterSet(FilterSet):
    # flag = MultipleChoiceFilter(choices=CHOICES)
    channel_of_usage = MultipleChoiceFilter(choices=CHANNEL)
    rating = MultipleChoiceFilter(choices=RATING)

    class Meta:
        model = Cooperation
        fields = {
        }
