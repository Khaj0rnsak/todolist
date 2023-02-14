from django.urls import include, path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('maxintarr/', MaxintArr.as_view() ,name="MaxintArr"),
    path('factorial/', Factorial.as_view() ,name="Factorial"),
    path('send-email/', EmailAPI.as_view() ,name="EmailAPI"),
]