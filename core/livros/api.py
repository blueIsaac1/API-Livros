from ninja import Router, Query
from .schemas import LivrosSchema, AvaliacaoSchema, FiltrosSortear
from . models import Livros, Categories

livros_router = Router()

@livros_router.get('/', response={200: dict, 400: dict})
def get_livro(request):
    livros = Livros.objects.all()
    # Serializando objetos usando LivrosSchema
    livros_data = [LivrosSchema.from_orm(livro).dict() for livro in livros]
    return {"response": livros_data}

# @livros_router.get("/avaliacoes/{livro_id}", response={200: list[AvaliacaoSchema], 404: dict})
# def listar_avaliacoes(request, livro_id: int):
#     livros = Livros.objects.get(id=livro_id)
#     # Serializando objetos usando LivrosSchema
#     livros_avaliacao =  livros.Ava.all()
#     return {"response": livros_avaliacao}


@livros_router.post('/', response={200: dict, 400: dict})
def create_book(request, livro_schema: LivrosSchema):
    id = livro_schema.id
    name = livro_schema.name
    streaming = livro_schema.streaming
    categories = livro_schema.categorie

    if streaming not in ['Fisico', 'Amazon Kindle']:                   
        return 400, {"status": "erro", "message": "Streaming inválido."}                        

    livro = Livros(name=name, streaming=streaming)
    livro.save()

    for cat_id in categories:
        try:
            cat_temp = Categories.objects.get(id=cat_id)
            livro.categorie.add(cat_temp)
        except Categories.DoesNotExist:         
            return 400, {"status": "erro", "message": f"Categoria com id {cat_id} não encontrada."}

    return 200, {"status": "ok", "message": "Livro criado com sucesso"}

@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id: int, avaliacao_schema: AvaliacaoSchema):
    comentarios = avaliacao_schema.dict()['comments']
    nota = avaliacao_schema.dict()['note']

    livro = Livros.objects.get(id=livro_id)
    livro.comments = comentarios
    livro.note = nota  # Corrigido para "note"
    livro.save()

    return 200, ['status', 'ok']


@livros_router.delete('/{livro_id}')
def deletar_livros(request, livro_id: int):
    livro = Livros.objects.get(id=livro_id)
    livro.delete()  # Corrigido para "delete()"

    return 200, {'status': 'deleted', 'id': livro_id}

@livros_router.get('/sortear/', response={200: LivrosSchema, 404: dict})
def sortear_livro(request, filtros: Query[FiltrosSortear]):
    nota_minima = filtros.dict().get('nota_minima')
    categoria = filtros.dict().get('categoria')
    reler = filtros.dict().get('reler', False)

    livros = Livros.objects.all()
    if not reler:
        livros = livros.filter(nota=None)

    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)
    
    if categoria:
        livros = livros.filter(categorie__id=categoria)

    livro = livros.order_by('?').first()

    if livro:
        return 200, LivrosSchema.from_orm(livro).dict()
    else:
        return 404, {'status': 'erro', 'message': 'Nenhum livro encontrado.'}
