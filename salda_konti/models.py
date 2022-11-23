from django.db import models

class SaldaKonti(models.Model):
    sifra=models.TextField(max_length=100, blank=True)
    naziv=models.TextField(max_length=100, blank=True)
    duguje=models.TextField(max_length=100, blank=True)
    potrazuje=models.TextField(max_length=100, blank=True)
    saldo=models.TextField(max_length=100, blank=True)
    dug=models.FloatField()
    pot=models.FloatField()
    sal=models.FloatField()
    