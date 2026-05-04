from django.contrib import admin

from .models import Leccion, Habilidad, Ejercicios, DominioHabilidad, Intento, Progreso,Explicacion, Intento

admin.site.register(Leccion)
admin.site.register(Habilidad)
admin.site.register(Ejercicios)
admin.site.register(Progreso)
admin.site.register(Intento)
class EjerciciosAdmin(admin.ModelAdmin):
    pass
admin.site.register(DominioHabilidad)
admin.site.register(Explicacion)