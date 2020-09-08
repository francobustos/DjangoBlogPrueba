# Generated by Django 3.1.1 on 2020-09-08 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=90, verbose_name='Título')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=110, verbose_name='Descripción')),
                ('body', models.TextField(verbose_name='Contenido')),
                ('image', models.URLField(default='https://i.insider.com/5e600587a9f40c6f39701245?width=600&format=jpeg&auto=webp')),
                ('state', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
