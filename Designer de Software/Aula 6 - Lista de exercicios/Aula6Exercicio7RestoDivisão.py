def quociente_resto_divisao():
    val1 = int(input('primeiro valor:'))
    val2 = int(input('segundo valor:'))
    
    quociente = val1 / val2
    resto = val1 % val2
    print(f'divisão de {val1} por {val2}:\n resultado: {quociente}\n resto: {resto}')
quociente_resto_divisao()