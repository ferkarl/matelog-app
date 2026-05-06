from django.db import models
from django.contrib.auth.models import User


# ------------------------------
# Habilidad
# ------------------------------
class Habilidad(models.Model):
    id_habilidad = models.AutoField(primary_key=True)
    nombre_habilidad = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'habilidad'

    def __str__(self):
        return self.nombre_habilidad


# ------------------------------
# Dominio Habilidad
# ------------------------------
class DominioHabilidad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_usuario')
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE, db_column='id_habilidad')
    nivel_dominio = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'dominio_habilidad'
        managed = False
        default_permissions = ()

# ------------------------------
# Lección
# ------------------------------
class Leccion(models.Model):
    id_leccion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    nivel = models.IntegerField()

    class Meta:
        db_table = 'leccion'

    def __str__(self):
        return self.titulo


# ------------------------------
# Explicación
# ------------------------------
class Explicacion(models.Model):
    id_explicacion = models.AutoField(primary_key=True)
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        db_column='id_leccion'
    )
    contenido = models.TextField()
    orden = models.IntegerField()
    tipo = models.CharField(max_length=50, null=True, blank=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'explicaciones'

    def __str__(self):
        return f"Explicación {self.id_explicacion}"


# ------------------------------
# Ejercicios
# ------------------------------
class Ejercicios(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    respuesta_correcta = models.TextField()
    tipo = models.CharField(max_length=50)
    tipo_ejercicio = models.CharField(max_length=20, default='normal')
    datos = models.JSONField(default=dict)
    orden = models.IntegerField(default=0)

    id_leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        db_column='id_leccion'
    )

    explicacion = models.ForeignKey(
        Explicacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    habilidades = models.ManyToManyField(
        Habilidad,
        through='EjercicioHabilidad'
    )

    class Meta:
        db_table = 'ejercicios'

    def __str__(self):
        return f"Ejercicio {self.id_ejercicio}"


# ------------------------------
# EjercicioHabilidad
# ------------------------------
class EjercicioHabilidad(models.Model):
    id_ejercicio = models.ForeignKey(Ejercicios, on_delete=models.CASCADE, db_column='id_ejercicio')
    id_habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE, db_column='id_habilidad')

    class Meta:
        db_table = 'ejercicio_habilidad'
        managed = False
        unique_together = ('id_ejercicio', 'id_habilidad')

# ------------------------------
# Intento
# ------------------------------
class Intento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicios, on_delete=models.CASCADE)
    es_correcto = models.BooleanField()
    tiempo_respuesta = models.IntegerField(default=0)
    numero_intento = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'intento'

    def __str__(self):
        return f"{self.usuario} - {self.ejercicio}"


# ------------------------------
# Progreso
# ------------------------------
class Progreso(models.Model):
    id_progreso = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)

    porcentaje_completado = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'progreso'
        unique_together = ('usuario', 'leccion')