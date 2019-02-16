def converte_tempo(minutos, segundos, milesimos):
    if milesimos >= 1000:
        segundos += (milesimos // 1000)
        milesimos = (milesimos % 1000)
    if segundos >= 60:
        minutos += (segundos // 60)
        segundos = (segundos % 60)
    return f'{minutos}:{segundos:02d}.{milesimos:03d}'


def calcula_tempo_total(listaDeTempos):
    total = {}
    for i in listaDeTempos:
        minuto = 0
        segundo = 0
        milesimo = 0
        for t in listaDeTempos[i]:
            t = t.replace(':', ' ')
            t = t.replace('.', ' ')
            t = t.split()

            minuto += int(t[0])
            segundo += int(t[1])
            milesimo += int(t[2])

        total[i] = converte_tempo(minuto, segundo, milesimo)
    return total