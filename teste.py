from models.cliente import Cliente
from models.conta import Conta

felipe: Cliente = Cliente('Felipe Guimares', 'felipe.live@gmai.com', '321.354.542-01', '11/05/2000')
gabriel: Cliente = Cliente('Gabriel Guedes', 'gabriel.guedes@gmail.com', '532.352.321.02', '30/06/2001')

contaf: Conta = Conta(felipe)
contaa: Conta = Conta(gabriel)

print(contaf)
print(contaa)