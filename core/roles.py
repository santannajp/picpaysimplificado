from rolepermissions.roles import AbstractUserRole

class People(AbstractUserRole):
    avaiable_permissions = {
        'make_transfer': True,
        'receive_transfer': True
    }

class Company(AbstractUserRole):
    avaiable_permissions = {
        'make_transfer': False,
        'receive_transfer': True
    }