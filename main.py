from trata_arquivo import obtem_arquivo
from extrai_dados import extrai_dados
from calculos import calcula_tempo_total
from ranking import exibe_ranking

log = obtem_arquivo()
dados = extrai_dados(log)
tempoTotal = calcula_tempo_total(dados[1])
exibe_ranking(tempoTotal, dados[0])