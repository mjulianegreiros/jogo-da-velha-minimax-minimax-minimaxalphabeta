# Regras.py

from tabuleiro import obterJogadasValidas

def verificarVitoria(tabuleiro: list , icone:str):
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0] == icone and tabuleiro[i][1] == icone and tabuleiro[i][2] == icone:
            return True
        
    for i in range(len(tabuleiro)):
        if tabuleiro[0][i] == icone and tabuleiro[1][i] == icone and tabuleiro[2][i] == icone:
            return True
    
    if tabuleiro[0][0] == icone and tabuleiro [1][1] == icone and tabuleiro[2][2] == icone:
        return True
    
    if tabuleiro[2][0] == icone and tabuleiro [1][1] == icone and tabuleiro[0][2] == icone:
        return True

    return False

def verificarEmpate(tabuleiro: list):
    jogadasValidas = obterJogadasValidas(tabuleiro=tabuleiro)

    if(len(jogadasValidas) != 0):
        return False
    
    return True

def verificarEstadoAtual(tabuleiro: list):
    if verificarVitoria(tabuleiro=tabuleiro, icone="X"):
        return "X venceu"
    elif verificarVitoria(tabuleiro=tabuleiro, icone="O"):
        return "O venceu"
    elif verificarEmpate(tabuleiro=tabuleiro):
        return "Empate"
    else:
        return "Em andamento"
    
def obterProxJogador(jogadorAtual:str):
    if jogadorAtual == "X":
        return "O"
    elif jogadorAtual == "O":
        return "X"
    else:
        print("Jogador inválido.")
        return None 