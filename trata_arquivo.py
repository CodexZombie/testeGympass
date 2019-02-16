def remove_espacos_extras(arquivo):
    novoArquivo = []
    for linha in arquivo:
        while '  ' in linha:
            linha = linha.replace('\t', ' ')
            linha = linha.replace('  ', ' ')
        novoArquivo.append(linha)
    return novoArquivo

def linhas_para_lista(arquivo):
    lista = []
    for linha in arquivo:
        linha = linha.rstrip()
        linha = linha.split(' ')
        lista.append(linha)
    lista.pop(0)
    return lista


def obtem_arquivo():
    arquivo = input('Informe a url do arquivo: ')
    log = open(arquivo, 'r')
    logCorrida = remove_espacos_extras(log)
    lista = linhas_para_lista(logCorrida)
    log.close()
    return lista

# LOCAL DO LOG: C:\Users\walve\Desktop\TesteGympass\corrida.log