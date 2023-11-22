from django.urls import path
from smart_pig.views import index, porco, reg_porco, rel_porco

urlpatterns = [
    path('', index, name='index'),
    path('porco', porco, name='porco'),
    path('reg_porco', reg_porco, name="reg_porco"),
    path('rel_porco', rel_porco, name='rel_porco')
]
