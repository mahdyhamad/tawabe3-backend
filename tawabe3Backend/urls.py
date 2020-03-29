from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from myapp.views import OrderViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),    
]