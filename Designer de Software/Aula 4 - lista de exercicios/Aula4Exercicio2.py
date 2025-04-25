def lista_parametro(lista):
    
    for x, parametro in enumerate(lista, start=1):
        print(f'indice: {x} iten da lista: {parametro}')
itens = ["maçã", 2, 'doce', 4, 5]
lista_parametro(itens)