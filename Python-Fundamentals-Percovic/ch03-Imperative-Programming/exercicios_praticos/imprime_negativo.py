
def imprime_negativo(lista):
    for item in lista:
        if item < 0:
            print(item)

lista = [4,0,-1, -3, 6, -9]

imprime_negativo(lista)