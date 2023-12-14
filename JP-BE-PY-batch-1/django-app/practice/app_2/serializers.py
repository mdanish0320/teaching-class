from rest_framework import serializers
from . models import EmployeeModel, DepartmentModel, SalaryModel

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = EmployeeModel
        depth = 1


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DepartmentModel



class SalarySerializer(serializers.ModelSerializer):
    employee_id = EmployeeSerializer(many=False, read_only=True)
    class Meta:
        fields = ['salary_date', 'employee_id']
        model = SalaryModel
        


        