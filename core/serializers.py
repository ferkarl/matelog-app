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

    id_leccion = serializers.IntegerField(source='leccion.id_leccion')
    explicacion_id = serializers.IntegerField(source='explicacion.id_explicacion', required=False)

    class Meta:
        model = Ejercicios
        fields = [
            'id_ejercicio',
            'pregunta',
            'respuesta_correcta',
            'tipo',
            'tipo_ejercicio',
            'datos',
            'orden',
            'id_leccion',
            'explicacion_id'
        ]