def list_num():
    lista_numeros = [1, 2, 3, 4]
    filtro_num_impar = filter(lambda x: x % 2 == 0, lista_numeros)
    print(list(filtro_num_impar))
list_num()