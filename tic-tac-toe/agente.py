# Agente.py

from tabuleiro import obterJogadasValidas
from minimax import escolherMelhorJogada

def escolherJogadaRobo(tabuleiro: list, robo: str):
    jogadas = obterJogadasValidas(tabuleiro)

    melhorJogada = escolherMelhorJogada(tabuleiro, robo)

    return melhorJogada