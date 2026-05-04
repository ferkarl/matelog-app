from core.models import Ejercicios

def run():
    for ej in Ejercicios.objects.all():
        datos = ej.datos or {}
        pregunta = (ej.pregunta or "").lower()

        # 🔹 detectar tipo visual
        if "opciones" in datos:
            if datos["opciones"] == ["Verdadera", "Falsa"]:
                ej.tipo = "verdadero_falso"
            else:
                ej.tipo = "opcion_multiple"

        elif "estructura" in datos:
            ej.tipo = "completar"

        elif "pistas" in datos:
            if "ordena" in pregunta or "orden" in pregunta:
                ej.tipo = "ordenar"
            else:
                ej.tipo = "texto"

        else:
            ej.tipo = "texto"

        # 🔹 asegurar tipo_ejercicio
        if not ej.tipo_ejercicio:
            ej.tipo_ejercicio = "normal"

        ej.save()

    print("Todos los ejercicios corregidos")