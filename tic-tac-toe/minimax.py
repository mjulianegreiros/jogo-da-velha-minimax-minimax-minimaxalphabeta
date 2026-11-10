# Minimax.py

from tabuleiro import obterJogadasValidas, aplicarJogada
from regras import verificarEstadoAtual , obterProxJogador

def avaliarTabuleiro(tabuleiro: list):
    estado = verificarEstadoAtual(tabuleiro=tabuleiro)

    if estado == "Empate":
        return 0
    elif estado == "X venceu":
        return 1
    elif estado == "O venceu":
        return -1
    else:
        return None
    
def minimax(tabuleiro: list, jogador: str , contador: list):
    resultado = avaliarTabuleiro(tabuleiro)

    contador[0] += 1
    # Caso terminal: retorna a pontuação.
    if resultado is not None:
        return resultado

    jogadasValidas = obterJogadasValidas(tabuleiro)
    resultados = []

    for jogada in jogadasValidas:

        # Cria uma cópia independente para a simulação.
        copia = [linha.copy() for linha in tabuleiro]

        # Aplica a jogada do jogador atual.
        copia = aplicarJogada(copia, jogada, jogador)

        # Alterna o jogador.
        proximoJogador = obterProxJogador(jogador)

        # Explora recursivamente a próxima situação.
        resultadoJogada = minimax(copia, proximoJogador , contador)

        resultados.append(resultadoJogada)

    # print(resultados)
    # X maximiza o resultado.
    if jogador == "X":
        return max(resultados)

    # O minimiza o resultado.
    else:
        return min(resultados)
    
def escolherMelhorJogada(tabuleiro: list, jogador: str, contador: list):
    jogadasValidas = obterJogadasValidas(tabuleiro=tabuleiro)
    melhorValor = None
    melhorJogada = None

    for jogada in jogadasValidas:
        copia = [linha.copy() for linha in tabuleiro]
        copia = aplicarJogada(copia, jogada, jogador)

        m = minimax(copia, obterProxJogador(jogador), contador)

        if melhorValor is None:
            melhorValor = m
            melhorJogada = jogada
        elif jogador == "X" and m > melhorValor:
            melhorValor = m
            melhorJogada = jogada
        elif jogador == "O" and m < melhorValor:
            melhorValor = m
            melhorJogada = jogada

    return melhorJogada , melhorValor




def minimaxAlfaBeta(tabuleiro: list, jogador: str, alfa: float, beta: float, contador: list):
    resultado = avaliarTabuleiro(tabuleiro)
    contador[0] += 1

    # Caso terminal
    if resultado is not None:
        return resultado

    jogadasValidas = obterJogadasValidas(tabuleiro)

    if jogador == "X":
        melhorValor = float("-inf")
    else:
        melhorValor = float("inf")

    for jogada in jogadasValidas:
        copia = [linha.copy() for linha in tabuleiro]
        copia = aplicarJogada(copia, jogada, jogador)

        proximoJogador = obterProxJogador(jogador)

        resultadoJogada = minimaxAlfaBeta(
            copia, proximoJogador, alfa, beta, contador
        )

        if jogador == "X":
            melhorValor = max(melhorValor, resultadoJogada)
            alfa = max(alfa, melhorValor)
        else:
            melhorValor = min(melhorValor, resultadoJogada)
            beta = min(beta, melhorValor)

        if alfa >= beta:
            break

    return melhorValor

    

def escolherMelhorJogadaAlfaBeta(tabuleiro: list, jogador: str, contador: list):
    jogadasValidas = obterJogadasValidas(tabuleiro=tabuleiro)
    melhorValor = None
    melhorJogada = None

    for jogada in jogadasValidas:
        copia = [linha.copy() for linha in tabuleiro]
        copia = aplicarJogada(copia, jogada, jogador)

        m = minimaxAlfaBeta(
            copia,
            obterProxJogador(jogador),
            float("-inf"),
            float("inf"),
            contador
        )

        if melhorValor is None:
            melhorValor = m
            melhorJogada = jogada
        elif jogador == "X" and m > melhorValor:
            melhorValor = m
            melhorJogada = jogada
        elif jogador == "O" and m < melhorValor:
            melhorValor = m
            melhorJogada = jogada

    return melhorJogada , melhorValor
