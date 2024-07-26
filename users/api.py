from ninja import Router

users_router = Router()

#receber nome do usuario e decorar resposta
@users_router.post('/', response={200: dict})
def create_user(request):
    return {'ok': 'ok'}