from rest_framework.routers import DefaultRouter
# 
from . import viewsets
# code
router = DefaultRouter()
router.register(r'viveros', viewsets.ViveroViewSet, basename='viveros')

# url_Imagenes = routerImagenes.get_urls()

urlpatterns = router.get_urls()