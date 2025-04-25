def cont_num_frut():
    lista = ['Maçã', 'Banana', 'Amora', 'Caqui']
    
    # Filtra as frutas com mais de 5 letras
    frutas_filtradas = filter(lambda fruta: len(fruta) > 5, lista)
    
    # Transforma as frutas filtradas em listas de letras
    frutas_transformadas = list(map(list, frutas_filtradas))
    
    print(frutas_transformadas)
cont_num_frut()