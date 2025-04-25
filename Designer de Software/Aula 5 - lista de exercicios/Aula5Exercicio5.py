media = float(input('Digite a nota do aluno (0 a 10):'))


if media >= 0 and media <= 4:
    nota = 'D'
if media >=5 and media <= 6:
    nota = 'C'
if media >= 7 and media <= 8:
    nota = 'B'
if media >= 9 and media<= 10:
    nota = 'A'
        
if nota:
    print(f'Nota: {nota} ({media})')
else:
    print('Nota inválida')
    