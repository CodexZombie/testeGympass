def exibe_ranking(tempoTotal, nomeEVoltas):
    ordemDeChegada = sorted(tempoTotal, key = tempoTotal.get)

    print('{:<10}{:^20}{:^23}{:>}'.format(
        'posição','piloto','voltas completadas', 'tempo total').upper())

    ranking = 0
    for numero in ordemDeChegada:
        ranking += 1
        nome = ''
        voltas = ''
        for piloto in nomeEVoltas[numero]:
            nome = piloto
            voltas = nomeEVoltas[numero][piloto]

        piloto = numero + ' - ' + nome
        print(f'{ranking:^7}     {piloto:<20}{voltas:^18}{tempoTotal[numero]:>14}')