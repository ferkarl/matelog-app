from django.core.management.base import BaseCommand
from core.models import Ejercicios
from core.utils.ejercicios import ejercicios_data

from django.core.management.base import BaseCommand
from core.models import Ejercicios
from core.utils.ejercicios import ejercicios_data

class Command(BaseCommand):
    help = 'Crear ejercicios de prueba'

    def handle(self, *args, **options):
        for index, data in enumerate(ejercicios_data):
            Ejercicios.objects.create(
                pregunta=data["pregunta"],
                respuesta_correcta=data["respuesta_correcta"],

                tipo=data.get("tipo", "texto"),  # UI (Flutter)
                tipo_ejercicio=data.get("tipo_ejercicio", "normal"),  # lógica

                datos=data.get("datos", {}),
                orden=index
            )

        self.stdout.write(self.style.SUCCESS('Ejercicios creados correctamente'))