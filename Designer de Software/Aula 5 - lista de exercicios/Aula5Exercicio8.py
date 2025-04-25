print('''
Qualquer pessoa que passe, uma ou duas, deve passar com a lanterna na mão. A lanterna deve ser levada de um lado para o outro, e não pode ser jogada, etc. Cada membro da banda tem um
tempo diferente para passar de um lado para o outro. O par deve andar junto no tempo do menos veloz:
''')
print('''
- Bono: 1 minuto para passar
- Edge: 2 minutos para passar
- Adam: 5 minutos para passar
- Larry: 10 minutos para passar\n
''')

def travessia_interativa():
    import time

    esquerda = ['Bono', 'Edge', 'Adam', 'Larry']
    tempos = {'Bono': 1, 'Edge': 2, 'Adam': 5, 'Larry': 10}
    direita = []
    total_tempo = 0
    lanterna_lado = 'esquerda'

    print("🎸 Início da travessia da banda U2")
    print("Todos estão no lado ESQUERDO da ponte.")
    print("A lanterna deve estar com quem vai atravessar.")
    print("Você pode escolher 1 ou 2 pessoas por vez.\n")

    while len(direita) < 4:
        print(f"⏱ Tempo atual: {total_tempo} minutos")
        print(f"📍 Lanterna está do lado: {lanterna_lado.upper()}")
        print(f"👥 Esquerda: {', '.join(esquerda) if esquerda else 'ninguém'}")
        print(f"👥 Direita: {', '.join(direita) if direita else 'ninguém'}\n")

        if lanterna_lado == 'esquerda':
            disponiveis = esquerda
        else:
            disponiveis = direita

        nomes = input(f"Digite 1 ou 2 nomes para atravessar do lado {lanterna_lado.upper()} (separados por vírgula): ").split(',')

        nomes = [nome.strip().capitalize() for nome in nomes if nome.strip()]

        if not (1 <= len(nomes) <= 2):
            print("❌ Você deve digitar 1 ou 2 nomes válidos.\n")
            continue

        if any(nome not in disponiveis for nome in nomes):
            print("❌ Um ou mais nomes não estão do lado correto. Tente novamente.\n")
            continue

        tempo_rodada = max(tempos[nome] for nome in nomes)
        total_tempo += tempo_rodada

        print(f"\n🚶 {', '.join(nomes)} atravessaram a ponte em {tempo_rodada} minutos.\n")

        for nome in nomes:
            if lanterna_lado == 'esquerda':
                esquerda.remove(nome)
                direita.append(nome)
            else:
                direita.remove(nome)
                esquerda.append(nome)

        # Lanterna muda de lado
        lanterna_lado = 'direita' if lanterna_lado == 'esquerda' else 'esquerda'

    print(f"\n✅ Todos atravessaram!")
    print(f"🕓 Tempo total gasto: {total_tempo} minutos")
    if total_tempo > 20:
        print("⚠️ O show vai atrasar!")
    else:
        print("🎉 Eles chegaram a tempo do show!")

travessia_interativa()
