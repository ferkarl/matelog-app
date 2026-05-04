# serializers.py
# Este archivo convierte los modelos de Django en formato JSON,
# permitiendo que los datos puedan ser enviados y utilizados por aplicaciones externas como Flutter.


from rest_framework import serializers
from .models import Leccion, Ejercicios, Explicacion

#lecciones 
class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'

#explicaciones

from rest_framework import serializers
from .models import Explicacion

class ExplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explicacion
        fields = '__all__'

from rest_framework import serializers
from .models import Ejercicios, Habilidad
 
#habilidad
class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = '__all__'

#ejercicios 
class EjerciciosSerializer(serializers.ModelSerializer):
    habilidades = HabilidadSerializer(many=True, read_only=True)

    class Meta:
        model = Ejercicios
        fields = '__all__'