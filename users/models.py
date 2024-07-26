from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from .validators import validate_cpf

# Create your models here.
#sobrescerevendo a classe Abstracted user para colocar o email como unique e o cpf

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, validators= [validate_cpf])
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0.00))

    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)

    def pay(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError("Value deve ser um decimal")
        
        self.amount -= value
        #aqui poderia entrar um self.save, porem trabalharemos com atomicidade, as alterações serão feitas quando a transferencia for completada, caso contrario farei um rollback

    def receive(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError("Value deve ser um decimal")
        
        self.amount += value    
    pass