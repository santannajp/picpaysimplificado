from ninja import Router
from .schemas import UserSchema

users_router = Router()

#receber nome do usuario e decorar resposta
@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    print(user.dict())
    return {'ok': 'ok'}