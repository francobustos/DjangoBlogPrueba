from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('generales/', generals, name = 'generals'),
    path('anime/', anime, name = 'anime'),
    path('piano/', piano, name = 'piano'),
    path('literatura/', literature, name = 'literature'),
]
