from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField("Nombre de la categoría", max_length = 100, null = False, blank = False)
    state = models.BooleanField("Categoría Activada/Categoría no Activada", default = True)
    creation_date = models.DateField("Fecha de Creación", auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key = True)
    names = models.CharField("Nombres del Autor", max_length = 255, null = False, blank = False)
    last_names = models.CharField('Apellidos del Autor', max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    email = models.EmailField('Correo Electrónico', null = True, blank = True)
    state = models.BooleanField("Autor Activo/No Activo", default = True)
    creation_date = models.DateField("Fecha de Cración", auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.last_names, self.names)
