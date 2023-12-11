from rest_framework import serializers
from app_1.models import Person
class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = "__all__"