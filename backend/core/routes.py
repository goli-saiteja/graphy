from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .viewsets import  getMetrics, getDepartments, insert

router = DefaultRouter()
router.register(r'metrics', getMetrics)
router.register(r'departments', getDepartments)

urlpatterns = [
    path('', include(router.urls)),
    path('insert/', insert, name='home'),
]