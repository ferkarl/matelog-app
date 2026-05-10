from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Ejercicios, Intento, Leccion, Explicacion
from .serializers import (
    EjerciciosSerializer,
    LeccionSerializer,
    ExplicacionSerializer
)


# =========================
# HOME STATS
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_stats(request):
    user = request.user

    total_ejercicios = Ejercicios.objects.count()

    correctos = Intento.objects.filter(
        usuario=user,
        es_correcto=True
    ).values('ejercicio_id').distinct().count()

    fallos = Intento.objects.filter(
        usuario=user,
        es_correcto=False
    ).count()

    score = correctos - (fallos * 0.1)

    progreso = 0
    if total_ejercicios > 0:
        progreso = score / total_ejercicios

    progreso = max(0, min(progreso, 1))

    return Response({
        "completados": correctos,
        "intentos": Intento.objects.filter(usuario=user).count(),
        "errores": fallos,
        "progreso": round(progreso, 2)
    })


# =========================
# LECCION
# =========================
class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer
    pagination_class = None


# =========================
# EXPLICACION
# =========================
class ExplicacionViewSet(viewsets.ModelViewSet):
    queryset = Explicacion.objects.all()
    serializer_class = ExplicacionSerializer

    def get_queryset(self):
        queryset = Explicacion.objects.all()
        leccion_id = self.request.query_params.get('leccion')

        if leccion_id:
            queryset = queryset.filter(leccion_id=leccion_id)

        return queryset


# =========================
# EJERCICIOS
# =========================
class EjerciciosViewSet(viewsets.ModelViewSet):
    queryset = Ejercicios.objects.all()
    serializer_class = EjerciciosSerializer

    def get_queryset(self):
        queryset = Ejercicios.objects.all()
        leccion_id = self.request.query_params.get('leccion')

        if leccion_id:
            queryset = queryset.filter(id_leccion=leccion_id)

        return queryset


# =========================
# LOGIN
# =========================

@api_view(['POST'])
def login_view(request):

    print("BODY:", request.body)
    print("DATA:", request.data)

    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({
            'error': 'Faltan datos'
        }, status=400)

    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'success': True,
            'token': token.key,
            'user_id': user.id
        })

    return Response({
        'error': 'Credenciales inválidas'
    }, status=401)

# =========================
# REGISTER
# =========================
@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Faltan datos'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Usuario ya existe'}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({'success': True}, status=201)


# =========================
# GUARDAR INTENTO
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def guardar_intento(request):
    user = request.user

    ejercicio_id = request.data.get('ejercicio_id')
    es_correcto = request.data.get('es_correcto', False)
    tiempo = request.data.get('tiempo_respuesta', 0)
    numero_intento = request.data.get('numero_intento', 1)

    if not ejercicio_id:
        return Response({'error': 'Falta ejercicio_id'}, status=400)

    try:
        ejercicio = Ejercicios.objects.get(id_ejercicio=ejercicio_id)
    except Ejercicios.DoesNotExist:
        return Response({'error': 'Ejercicio no existe'}, status=404)

    Intento.objects.create(
        usuario=user,
        ejercicio=ejercicio,
        es_correcto = str(es_correcto).lower() == "true",
        tiempo_respuesta=tiempo,
        numero_intento=numero_intento
    )

    fallos = Intento.objects.filter(
        usuario=user,
        ejercicio=ejercicio,
        es_correcto=False
    ).count()

    return Response({
        "success": True,
        "refuerzo": fallos >= 2
    })