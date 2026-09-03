from django.urls import path
from .views import TopViewSet, TovarViewSet, home, index

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("top", TopViewSet, basename="top")
router.register("tovar", TovarViewSet, basename="tovar")

urlpatterns = [
    path("", home, name="home"),
    path("index/", index, name="index"),
]

urlpatterns += router.urls