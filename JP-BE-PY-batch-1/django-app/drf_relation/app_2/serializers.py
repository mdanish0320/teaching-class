from rest_framework import serializers
from .models import Employee, Project


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = "__all__"
    
    
class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = "__all__"
    depth = 1