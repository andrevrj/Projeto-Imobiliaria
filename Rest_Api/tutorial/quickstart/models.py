# Create your models here.

from django.db import models

import uuid


class Imovel(models.Model):
    SETOR_CHOICES = [
        ('apartamento', 'Apartamento'), ('kitnet', 'Kitnet'), ('casa', 'Casa'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    codigo = models.CharField(
        max_length=8,
        null=False,
        blank=False)

    tipo = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=SETOR_CHOICES)

    endereco = models.CharField(
        max_length=40,
        null=False,
        blank=False)

    valor = models.CharField(
        max_length=8,
        null=False,
        blank=False)


class Cliente(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    nome = models.CharField(
        max_length=40,
        null=False,
        blank=False)

    email = models.CharField(
        max_length=40,
        null=False,
        blank=False)

    telefone = models.CharField(
        max_length=8,
        null=False,
        blank=False,)

