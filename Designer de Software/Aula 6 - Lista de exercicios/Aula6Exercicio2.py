frutas = ['Maca', 'Banana', 'Uva', 'Melão', 'Mamão', 'Abacaxi', 'Laranja', 'Limão', 'Kiwi', 'Pera', 'Morango', 'Framboesa', 'Amora', 'Cereja', 'Jabuticaba', 'Goiaba', 'Abacate']
def filtro_list(lista):
    print(lista)
    
    letra = input('Vamos filtrar sua lista, digite uma letra:').strip().upper()

    filtro = [item for item in lista if item.upper().startswith(letra)]
    
    if filtro:
        print(f'Para letra: {letra} lista filtrada:\n {filtro}\n')
    else:
        print(f'Para letra: {letra} não há itens na lista \n')
    return filtro_list(lista)
filtro_list(frutas)
    
    