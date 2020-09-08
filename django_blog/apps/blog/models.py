from django.db import models
from ckeditor.fields import RichTextField

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
    creation_date = models.DateField("Fecha de Creación", auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.last_names, self.names)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Título', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    description = models.CharField('Descripción', max_length = 110, blank = True, null = False)
    body = RichTextField()
    image = models.URLField(default = 'https://i.insider.com/5e600587a9f40c6f39701245?width=600&format=jpeg&auto=webp')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    state = models.BooleanField('Publicado/No Publicado',default = True)
    creation_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
