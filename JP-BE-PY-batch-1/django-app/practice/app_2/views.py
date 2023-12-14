from django.shortcuts import render
from rest_framework import viewsets, response
from . models import EmployeeModel, DepartmentModel, SalaryModel
from . serializers import EmployeeSerializer, DepartmentSerializer, SalarySerializer

# Create your views here.
class Departmentmvc(viewsets.ModelViewSet):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer


class Employeemvc(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request):
        # fetch department_ids from json
        department_ids = request.data.pop('department_id', [])

        # add employee
        serialized_employee = EmployeeSerializer(data=request.data)
        if serialized_employee.is_valid(raise_exception=True):
            employee = serialized_employee.save()

        # add employee into department
        departments = DepartmentModel.objects.filter(id__in=department_ids).all()
        for dep in departments:
            employee.departments.add(dep)

        # response
        return response.Response(serialized_employee.data)
    
class Salarymvs(viewsets.ModelViewSet):
    queryset = SalaryModel.objects.all()
    serializer_class = SalarySerializer
