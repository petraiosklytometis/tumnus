
from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
  available_permissions = {
    'cadastrar_produtos': True,
    'liberar_descontos': True,
    'cadastrar_operador': True,
  }

class Operador(AbstractUserRole):
  available_permissions = {
    'realizar_vendas': True,
  }