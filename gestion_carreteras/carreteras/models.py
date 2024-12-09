from django.db import models


class CategoriaCarretera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Carretera(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.ForeignKey(CategoriaCarretera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


class Tramo(models.Model):
    carretera = models.ForeignKey(Carretera, on_delete=models.CASCADE)
    km_inicio = models.FloatField()
    km_termino = models.FloatField()
    comuna_inicio = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, related_name="tramos_inicio"
    )
    comuna_termino = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, related_name="tramos_termino"
    )
    es_inicio_carretera = models.BooleanField(default=False)
    es_fin_carretera = models.BooleanField(default=False)
    confluye_con = models.ForeignKey(
        Carretera,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="confluencias",
    )
    km_confluencia = models.FloatField(null=True, blank=True)
    comuna_confluencia = models.ForeignKey(
        Comuna,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="confluencias",
    )

    def __str__(self):
        return f"{self.carretera} (Km {self.km_inicio}-{self.km_termino})"
