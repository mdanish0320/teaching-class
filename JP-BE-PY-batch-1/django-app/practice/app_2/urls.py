from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import Departmentmvc, Employeemvc, Salarymvs

router = DefaultRouter()
router.register('employee/mvs', Employeemvc)
router.register('department/mvs', Departmentmvc)
router.register('salary/mvs', Salarymvs)

urlpatterns = [] + router.urls