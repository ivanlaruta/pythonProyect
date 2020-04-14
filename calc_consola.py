def suma(a, b):
    res = a + b
    print(res)


def resta(a, b):
    res = a - b
    print(res)


def multiplica(a, b):
    res = a * b
    print(res)


def divide(a, b):
    if b == 0:
        print('error!')
    else:
        res = a / b
        print(res)


sw = True
while sw:
    menu = '''
    ======== CALUCLADORA =======
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir '''
    print(menu)
    op = int(input('Ingrese una opcion... '))
    num1 = int(input('Ingrese primer numero... '))
    num2 = int(input('Ingrese segundo numero... '))
    if op == 1:
        suma(num1,num2)
    elif op == 2:
        resta(num1,num2)
    elif op == 3:
        multiplica(num1,num2)
    elif op == 4:
        divide(num1,num2)
    elif op == 5:
        print('Programa finalizado')
        sw = False
    else:
        print(f'La opción {op} no disponible')
