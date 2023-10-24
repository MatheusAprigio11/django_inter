from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)