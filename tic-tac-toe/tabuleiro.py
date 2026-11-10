# Tabuleiro.py

def criarTabuleiro():
    tabuleiro = [['_' , '_' , '_'] , ['_' , '_' , '_'] , ['_' , '_' , '_']]    
    return tabuleiro

def exibirTabuleiro(tabuleiro: list):
    for i in range(len(tabuleiro[0])):
        for j in range(len(tabuleiro[0])):
            print(tabuleiro[i][j] , end=" ")
        print("\n")

def obterJogadasValidas(tabuleiro: list):
    jogadas = []
    for i in range(len(tabuleiro[0])):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == '_':
                jogadas.append([i , j])
    # print(jogadas)
    return jogadas

def aplicarJogada(tabuleiro: list , jogada:list , icone:str):
    jogadasValidas = obterJogadasValidas(tabuleiro)

    if icone not in ["X" , "O"]:
        print(f"O ícone {icone} não é válido no jogo.")
        return tabuleiro

    if not isinstance(jogada, list):
        print("A jogada não tem estrutura válida.")
        return tabuleiro
    
    if len(jogada)!= 2:
        print("Não foi possível realizar essa jogada.")
        return tabuleiro
    
    if not isinstance(jogada[0], int) or not isinstance(jogada[1], int):
        print(f"A jogada {jogada} não tem estrutura válida.")
        return tabuleiro
    
    if (jogada[0] > 2 or jogada[0] < 0) or (jogada[1] > 2 or jogada[1] < 0):
        print(f"Não é possível inserir o ícone: {icone} na posição {jogada} pois ela não existe.")
        return tabuleiro

    if jogada in jogadasValidas:
        tabuleiro[jogada[0]][jogada[1]] = icone
    else:
        print(f"A posição {jogada} já está preenchida.")

    return tabuleiro
    

