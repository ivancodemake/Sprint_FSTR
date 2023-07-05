from django_filters import rest_framework as filters
from .models import Mountain


class MountainFilter(filters.FilterSet):
    user__email = filters.CharFilter(field_name='user__email')

    class Meta:
        model = Mountain
        fields = ['user__email']
