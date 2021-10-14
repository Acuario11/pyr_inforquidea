from rest_framework.routers import DefaultRouter
# 
from . import viewsets
# code
router = DefaultRouter()
router.register(r'orquideas', viewsets.OrquideaViewSet, basename='orquideas')

# url_Imagenes = routerImagenes.get_urls()

urlpatterns = router.get_urls()