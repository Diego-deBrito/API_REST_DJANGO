from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import MetricaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView





# Criação automática de rotas
router = DefaultRouter()
router.register(r'metricas', MetricaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # --- ROTAS DO SWAGGER ---
    
    # 1. O Arquivo de Schema (O "cérebro" em JSON/YAML)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # 2. A Interface Visual Swagger (A famosa tela azul/verde)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # 3. Interface Redoc (Uma alternativa mais limpa, opcional)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]