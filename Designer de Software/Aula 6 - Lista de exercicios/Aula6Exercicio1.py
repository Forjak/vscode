def Par_impar_true_false():
    num = float(input('Digite um numero:'))
    if num % 2 == 0:
        confirmação = True
    else:
        confirmação = False
    print(f'o numero {num} é par? {confirmação}')
    return Par_impar_true_false()
Par_impar_true_false()