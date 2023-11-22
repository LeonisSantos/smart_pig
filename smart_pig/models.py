from django.db import models

# Create your models here.


class Porco(models.Model):
    OPCOES_SEXO = [
        ("FEMEA", "Femea"),
        ("MACHO", "Macho")
    ]
    OPCOES_REPRODUTOR = [
        ("CASTRADO", "Castrado"),
        ("FÉRTIL", "Fértil"),
    ]

    data_nas = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(
        max_length=100, choices=OPCOES_SEXO, null=False, blank=False)
    peso = models.CharField(max_length=100, null=False, blank=False)
    reprodutivo = models.CharField(
        max_length=100, choices=OPCOES_REPRODUTOR, null=False, blank=False)
    vacinas = models.CharField(max_length=100, null=False, blank=False)
    medicamentos = models.CharField(max_length=100, null=False, blank=False)
    pai = models.CharField(max_length=100, null=False, blank=False)
    mae = models.CharField(max_length=100, null=False, blank=False)
