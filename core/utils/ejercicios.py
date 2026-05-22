# core/utils/ejercicios.py
# PRUEBA CAMBIO GITHUB
ejercicios_data = [
    {
        "pregunta": "El cielo es azul",
        "respuesta_correcta": "Sí es proposición",
        "tipo": "opcion_multiple",
        "tipo_ejercicio": "normal",
        "datos": {
            "opciones": ["Sí es proposición", "No es proposición"]
        }
    },
    {
        "pregunta": "10 es un número impar",
        "respuesta_correcta": "Falsa",
        "tipo": "verdadero_falso",
        "tipo_ejercicio": "normal",
        "datos": {
            "opciones": ["Verdadera", "Falsa"]
        }
    },
    {
        "pregunta": "Ordena las palabras: niños / juegan / parque",
        "respuesta_correcta": "Los niños juegan en el parque",
        "tipo": "texto",
        "tipo_ejercicio": "normal",
        "datos": {
            "pistas": ["niños", "juegan", "parque"]
        }
    },
    {
    "pregunta": "Llueve ___ hace frío",
    "tipo": "completar",
    "tipo_ejercicio": "normal",
    "datos": {
        "estructura": ["Llueve", "___", "hace frío"],
        "opciones": ["y", "o"],
        "respuestas_validas": [
            "Llueve y hace frío"
        ]
    }
},
    {
        "pregunta": "Los planetas giran alrededor del sol",
        "respuesta_correcta": "Verdadera",
        "tipo": "verdadero_falso",
        "tipo_ejercicio": "normal",
        "datos": {
            "opciones": ["Verdadera", "Falsa"]
        }
    },

    # REFUERZO
    {
        "pregunta": "Refuerzo 1 ejemplo",
        "respuesta_correcta": "Sí",
        "tipo": "opcion_multiple",
        "tipo_ejercicio": "refuerzo",
        "datos": {
            "opciones": ["Sí", "No"]
        }
    },
    {
        "pregunta": "Refuerzo 2 ejemplo",
        "respuesta_correcta": "No",
        "tipo": "opcion_multiple",
        "tipo_ejercicio": "refuerzo",
        "datos": {
            "opciones": ["Sí", "No"]
        }
    }
]