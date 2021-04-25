from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PostViewSet
from .views import analytics

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path("analytics/", analytics),
]
