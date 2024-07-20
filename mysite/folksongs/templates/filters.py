import django_filters

from .models import *


class SongFilter(django_filters.FilterSet):
    class Meta:
        model = Song
        fields = "__all__"
