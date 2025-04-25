def letras_contrarias():
    palavra = input(f'digite uma palavra:')
    
    lista_palvra = list(palavra)
    lista_palvra.reverse()
    
    print(lista_palvra)
letras_contrarias()