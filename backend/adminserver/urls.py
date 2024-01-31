from django.urls import include, re_path
from core import routes as core_routes

urlpatterns = [
    re_path(r'^api/', include(core_routes)),
]
