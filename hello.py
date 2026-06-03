print('saldo actual:1000')
cantidad = 1000
cantidad = int(input('ingrese la cantidad que quiere retirar: '))
if cantidad < 1000:
    print('retiro exitoso')
    cantidad = 1000 - cantidad
    print('saldo restante: ', cantidad)
else:
    print('error, fondos insuficientes')
    