from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import EjerciciosViewSet, LeccionViewSet, ExplicacionViewSet, login_view, register_view, home_stats
from .views import guardar_intento
from .views import ExplicacionViewSet

router = DefaultRouter()
router.register(r'ejercicios', EjerciciosViewSet)
router.register(r'lecciones', LeccionViewSet)
router.register(r'explicaciones', ExplicacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home_stats/', home_stats),
    path('login/', login_view), 
    path('register/', register_view), 
    path('intento/', guardar_intento),
]