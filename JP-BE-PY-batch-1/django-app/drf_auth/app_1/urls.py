from rest_framework.routers import DefaultRouter
from . views import Usermvs

router = DefaultRouter()
router.register("user", Usermvs, 'user')
router.register("user_2", Usermvs, 'user_2')
router.register("user_3", Usermvs, 'user_3')

urlpatterns = [] + router.urls