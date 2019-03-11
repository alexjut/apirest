from .models import Usuario
from .models import Pf

from rest_framework import  serializers 


class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario  
        fields = '__all__'
       

class PfSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pf  
        fields = '__all__'


