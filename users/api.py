from ninja import Router
from .schemas import UserSchema
from .models import User
from django.contrib.auth.hashers import make_password

users_router = Router()

#receber nome do usuario e decorar resposta
@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    user.full_clean()
    user.save()

    return {'ok': 'ok'}