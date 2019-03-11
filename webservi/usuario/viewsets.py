from rest_framework import viewsets

from .models import Usuario
from .serializer import UsuarioSerializer
from .models import Pf
from .serializer import PfSerializer

from .models import Pf


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset =  Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PfViewSet(viewsets.ModelViewSet):
    queryset =  Pf.objects.all()
    serializer_class = PfSerializer