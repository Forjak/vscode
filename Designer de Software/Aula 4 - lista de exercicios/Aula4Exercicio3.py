def parametro_lista(lista):
    
    for x, valor in enumerate (lista, start=1):
        print(f' {x}º numero - {valor}')
        
    media = sum (lista) / len(lista)
    print(f'Media entre eles: {media}')
itens = [10, 20, 30, 40, 50]

parametro_lista (itens)