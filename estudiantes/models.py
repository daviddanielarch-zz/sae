from django.db import models

ESTADO_CIVIL_CHOICES = [('1', '1 - Soltero/a'),
                        ('2', '2 - Casado/a'),
                        ('3', '3- Separado/a de hecho'),
                        ('4', '4 - Viudo/a'),
                        ('5', '5 - Divorciado/a'),
                        ('6', '6 - Unido/a de Hecho')]


class Familiar(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    facultad = models.CharField(max_length=256)
    estado_civil = models.CharField(max_length=32, choices=ESTADO_CIVIL_CHOICES)
    familia = models.ManyToManyField(Familiar)

    def __str__(self):
        return self.nombre


class Historia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    datos = models.TextField()

    def __str__(self):
        return '{} Historia'.format(self.estudiante.nombre)


class Tarea(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    datos = models.TextField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return 'Tarea creada para {}'.format(self.estudiante.nombre)
