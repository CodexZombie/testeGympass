class Volta:
    def __init__(self, num, nome, volta, tempo):
        self.numero = num
        self.nome = nome
        self.volta = volta
        self.tempo = tempo


def lista_de_voltas_para_objeto(lista):
    listaPilotos = []
    for i in lista:
        piloto = Volta(i[1], i[3], i[4], i[5])
        listaPilotos.append(piloto)
    return listaPilotos


def extrai_num_de_voltas(listaObj):
    numNomeVoltas = {}
    for idBuscado in listaObj:
        for piloto in listaObj:
            if idBuscado.numero not in piloto.numero:
                numNomeVoltas[idBuscado.numero] = {idBuscado.nome:idBuscado.volta}
    return numNomeVoltas


def consolida_voltas_por_piloto(voltasObj, numDeVoltas):
    tempoVoltas = {}
    for i in numDeVoltas:
        lista = {}
        tmp = []
        for p in voltasObj:
            if i in p.numero:
                tmp.append(p.tempo)
        lista.update({i:tmp})
        tempoVoltas.update(lista)
    return tempoVoltas


def extrai_dados(arquivo):
    voltasObj = lista_de_voltas_para_objeto(arquivo)
    numVoltas = extrai_num_de_voltas(voltasObj)
    voltasPorPiloto = consolida_voltas_por_piloto(voltasObj, numVoltas)
    return numVoltas, voltasPorPiloto