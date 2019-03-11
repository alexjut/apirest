from rest_framework import routers 

from .viewsets import UsuarioViewSet
from .viewsets import PfViewSet

routers = routers.SimpleRouter()

routers.register('usuario', UsuarioViewSet , PfViewSet )

urlpatterns = routers.urls