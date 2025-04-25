def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

numero = 10
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")