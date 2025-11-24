from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import MetricaViewSet

# Criação automática de rotas
router = DefaultRouter()
router.register(r'metricas', MetricaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]