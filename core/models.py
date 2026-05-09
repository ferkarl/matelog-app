from django.db import models
from django.contrib.auth.models import User


# ==============================
# HABILIDAD
# ==============================
class Habilidad(models.Model):
    id_habilidad = models.AutoField(primary_key=True)
    nombre_habilidad = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'habilidad'

    def __str__(self):
        return self.nombre_habilidad


# ==============================
# DOMINIO HABILIDAD
# ==============================
class DominioHabilidad(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='usuario_id'
    )
    habilidad = models.ForeignKey(
        Habilidad,
        on_delete=models.CASCADE,
        db_column='id_habilidad'
    )
    nivel_dominio = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'dominio_habilidad'
        unique_together = ('usuario', 'habilidad')

    def __str__(self):
        return f"{self.usuario} - {self.habilidad}"


# ==============================
# LECCIÓN
# ==============================
class Leccion(models.Model):
    id_leccion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    nivel = models.IntegerField()

    class Meta:
        db_table = 'leccion'

    def __str__(self):
        return self.titulo


# ==============================
# EXPLICACIÓN
# ==============================
class Explicacion(models.Model):
    id_explicacion = models.AutoField(primary_key=True)

    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        related_name='explicaciones',
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


# ==============================
# EJERCICIOS
# ==============================
class Ejercicios(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)

    pregunta = models.TextField()
    respuesta_correcta = models.TextField()
    tipo = models.CharField(max_length=50)
    tipo_ejercicio = models.CharField(max_length=20, default='normal')
    datos = models.JSONField(default=dict)
    orden = models.IntegerField(default=0)

    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        related_name='ejercicios',
        db_column='id_leccion'
    )

    explicacion = models.ForeignKey(
        Explicacion,
        on_delete=models.CASCADE,
        related_name='ejercicios',
        db_column='id_explicacion'
    )

    habilidades = models.ManyToManyField(
        Habilidad,
        through='EjercicioHabilidad'
    )

    class Meta:
        db_table = 'ejercicios'

    def __str__(self):
        return f"Ejercicio {self.id_ejercicio}"


# ==============================
# TABLA INTERMEDIA
# ==============================
class EjercicioHabilidad(models.Model):
    ejercicio = models.ForeignKey(
        Ejercicios,
        on_delete=models.CASCADE,
        db_column='id_ejercicio'
    )
    habilidad = models.ForeignKey(
        Habilidad,
        on_delete=models.CASCADE,
        db_column='id_habilidad'
    )

    class Meta:
        db_table = 'ejercicio_habilidad'
        unique_together = ('ejercicio', 'habilidad')

    def __str__(self):
        return f"{self.ejercicio} - {self.habilidad}"


# ==============================
# INTENTOS
# ==============================
class Intento(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='usuario_id'
    )
    ejercicio = models.ForeignKey(
        Ejercicios,
        on_delete=models.CASCADE,
        db_column='id_ejercicio'
    )

    es_correcto = models.BooleanField()
    tiempo_respuesta = models.IntegerField(default=0)
    numero_intento = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'intento'

    def __str__(self):
        return f"{self.usuario} - {self.ejercicio}"


# ==============================
# PROGRESO
# ==============================
class Progreso(models.Model):
    id_progreso = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='usuario_id'
    )
    leccion = models.ForeignKey(
        Leccion,
        on_delete=models.CASCADE,
        db_column='id_leccion'
    )

    porcentaje_completado = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'progreso'
        unique_together = ('usuario', 'leccion')

    def __str__(self):
        return f"{self.usuario} - {self.leccion}"