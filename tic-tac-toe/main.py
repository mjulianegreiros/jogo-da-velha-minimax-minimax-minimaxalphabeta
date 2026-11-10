# Main.py

import sys
from tabuleiro import criarTabuleiro , obterJogadasValidas , exibirTabuleiro , aplicarJogada
from interface import escolherSimbolo , solicitarJogada , escolherAlgoritmo , exibirResultados
from regras import obterProxJogador , verificarEstadoAtual
from minimax import escolherMelhorJogada , escolherMelhorJogadaAlfaBeta
import time



algoritmo = escolherAlgoritmo()
icone = escolherSimbolo()

if(icone == None):
    sys.exit()

tab = criarTabuleiro()

humano = icone
robo = ""

if icone == "X":
    robo = "O"
else:
    robo = "X"

atual = "X"

historicoNos = []
historicoTempos = []
historicoValores = []
historicoJogadas = []

while verificarEstadoAtual(tab) == "Em andamento":
    if atual == humano:
        jogada = solicitarJogada(tab)
    else:
        
        contador = [0]

        inicio = time.perf_counter()

        if algoritmo == 'alphabeta':
            jogada , valor = escolherMelhorJogadaAlfaBeta(
                tabuleiro=tab,
                jogador=robo,
                contador=contador
            )
        else:
            jogada , valor = escolherMelhorJogada(
                tabuleiro=tab,
                jogador=robo,
                contador=contador
            )

        fim = time.perf_counter()

        tempo = (fim - inicio) * 1000

        historicoTempos.append(tempo)
        historicoNos.append(contador[0])
        historicoValores.append(valor)
        historicoJogadas.append(jogada)
        # print(f"Algoritmo: {algoritmo}")
        # print(f"Nós visitados: {contador[0]}")
    
    antes = [linha.copy() for linha in tab]
    tab = aplicarJogada(tab , jogada , atual)

    if tab != antes:
        atual = obterProxJogador(atual)
    else:
        print("O jogador não foi alternado! Refaça sua jogada, desta vez, uma válida.")

    

estado = verificarEstadoAtual(tab)
exibirResultados(algoritmo , historicoJogadas , historicoValores , historicoNos , historicoTempos)
exibirTabuleiro(tab)
print(estado)
