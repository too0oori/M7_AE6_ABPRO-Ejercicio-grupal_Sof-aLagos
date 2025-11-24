from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    voluntarios = models.ManyToManyField('voluntarios.Voluntario', related_name='eventos', blank=True)
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo