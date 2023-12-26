from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("user", views.Usermvs, 'user')
router.register("user_2", views.Usermvs_2, 'user_2')
router.register("user_3", views.Usermvs_3, 'user_3')
router.register("user_4", views.Usermvs_4, 'user_4')

urlpatterns = [] + router.urls