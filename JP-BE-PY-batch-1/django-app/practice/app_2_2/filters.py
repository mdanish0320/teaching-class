from django_filters import FilterSet
from .models import AuthorModel

class AuthorFilter(FilterSet):
  class Meta:
    model = AuthorModel
    fields = {
      "fname": ['contains', 'exact'],
      "lname": ['contains', 'exact']
    }