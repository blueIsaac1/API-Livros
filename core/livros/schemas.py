# schemas.py
from ninja import ModelSchema, Schema
from .models import Livros

class LivrosSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['name', 'streaming', 'categorie']

class AvaliacaoSchema(ModelSchema):
    class Meta:
        model = Livros
        fields = ['note', 'comments']  # Corrigido para "note"

class FiltrosSortear(Schema):
    nota_minima: int = None
    categoria: int = None
    reler: bool = False
