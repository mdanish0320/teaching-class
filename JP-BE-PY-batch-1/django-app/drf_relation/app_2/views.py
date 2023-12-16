from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from datetime import datetime

from . models import Employee, Project
from . serializers import EmployeeSerializer, ProjectSerializer

# Create your views here.
class Employeemvs(ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  
  
class Projectmvs(ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  
  def create(self, request):
      # fetch department_ids from json
      emp_ids = request.data.pop('emp_ids', [])

      # add employee
      serialized_project = ProjectSerializer(data=request.data)
      if serialized_project.is_valid(raise_exception=True):
          project = serialized_project.save()

      # add employee into department
      employees = Employee.objects.filter(id__in=emp_ids).all()
      for emp in employees:
          project.employee.add(emp, through_defaults={"assignment_date": datetime.now().date(), "is_active": True})

      # response
      return Response(serialized_project.data)
