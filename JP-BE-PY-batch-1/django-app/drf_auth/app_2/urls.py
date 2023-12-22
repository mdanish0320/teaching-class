from rest_framework.routers import DefaultRouter
from . views import Usermvs

router = DefaultRouter()
router.register("user", Usermvs, 'user')

urlpatterns = [] + router.urls