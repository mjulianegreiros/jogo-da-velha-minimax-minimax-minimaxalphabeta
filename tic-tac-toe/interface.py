    # Interface.py

import os
from tabuleiro import obterJogadasValidas

# Cores ANSI
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
GREEN   = "\033[92m"
RED     = "\033[91m"
WHITE   = "\033[97m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def solicitarJogada(tabuleiro: list):
    """Solicita uma posição (1-9) e retorna [linha, coluna]."""
    while True:
        limpar()

        # Monta o tabuleiro dinamicamente
        celulas = []
        for i in range(9):
            l, c = i // 3, i % 3
            valor = tabuleiro[l][c]
            if valor == "X":
                celulas.append(f"{YELLOW}{BOLD}  X  {RESET}")
            elif valor == "O":
                celulas.append(f"{MAGENTA}{BOLD}  O  {RESET}")
            else:
                celulas.append(f"  {i+1}  ")

        print(f"""
{BOLD}{CYAN}
┌─────────────────────────────────┐
│                                 │
│      ✦  ESCOLHA A POSIÇÃO  ✦    │
│                                 │
{RESET}{BOLD}{WHITE}│         ┌─────┬─────┬─────┐      │
│         │{celulas[0]}│{celulas[1]}│{celulas[2]}│      │
│         ├─────┼─────┼─────┤      │
│         │{celulas[3]}│{celulas[4]}│{celulas[5]}│      │
│         ├─────┼─────┼─────┤      │
│         │{celulas[6]}│{celulas[7]}│{celulas[8]}│      │
│         └─────┴─────┴─────┘      │
{RESET}{DIM}
└─────────────────────────────────┘
""")
        pos = input(f"  {BOLD}{CYAN}➤{RESET} Posição (1-9): ").strip()

        if not pos.isdigit() or int(pos) < 1 or int(pos) > 9:
            print(f"\n  {RED}⚠ Entrada inválida. Digite um número de 1 a 9.{RESET}")
            input(f"\n  {DIM}Pressione ENTER para continuar...{RESET}")
            continue

        pos = int(pos)
        linha = (pos - 1) // 3
        coluna = (pos - 1) % 3

        jogadas_validas = obterJogadasValidas(tabuleiro)

        if [linha, coluna] not in jogadas_validas:
            ocupante = tabuleiro[linha][coluna]
            print(f"\n  {RED}⚠ Posição {BOLD}{pos}{RESET} já está ocupada por {BOLD}{ocupante}{RESET}! Escolha outra.{RESET}")
            input(f"\n  {DIM}Pressione ENTER para continuar...{RESET}")
            continue

        print(f"\n  {GREEN}✦{RESET} Posição {BOLD}{pos}{RESET} → coordenadas: {BOLD}{WHITE}[{linha}, {coluna}]{RESET}")
        return [linha, coluna]   
    
def escolherSimbolo():
    while True:
        limpar()
        print(f"""
{BOLD}{CYAN}
┌─────────────────────────────────┐
│                                 │
│         ✦  M E N U  ✦           │
│                                 │
{RESET}{BOLD}{YELLOW}│   1)  X                         │
{RESET}{BOLD}{MAGENTA}│   2)  O                         │
{RESET}{BOLD}{RED}│   3)  Sair                      │
{RESET}{DIM}
└─────────────────────────────────┘
""")
        opcao = input(f"  {BOLD}{CYAN}➤{RESET} Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"\n  {GREEN}✦{RESET} Você escolheu: {BOLD}X{RESET}")
            return "X"
        elif opcao == "2":
            print(f"\n  {GREEN}✦{RESET} Você escolheu: {BOLD}O{RESET}")
            return "O"
        elif opcao == "3":
            print(f"\n  {MAGENTA}✦{RESET} Até logo! {WHITE}👋{RESET}\n")
            return None
        else:
            print(f"\n  {RED}⚠{RESET} Opção inválida, tente novamente.")
            input(f"\n  {DIM}Pressione ENTER para continuar...{RESET}")

def escolherAlgoritmo():
    while True:
        limpar()
        print(f"""
{BOLD}{CYAN}
┌─────────────────────────────────┐
│                                 │
│         ✦  M E N U  ✦           │
│                                 │
{RESET}{BOLD}{YELLOW}│   1)  Minimax                   │
{RESET}{BOLD}{MAGENTA}│   2)  Minimax Alfa-Beta         │
{RESET}{DIM}
└─────────────────────────────────┘
""")
        opcao = input(f"  {BOLD}{CYAN}➤{RESET} Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"\n  {GREEN}✦{RESET} Algoritmo: {BOLD}Minimax{RESET}")
            return "minimax"
        elif opcao == "2":
            print(f"\n  {GREEN}✦{RESET} Algoritmo: {BOLD}Minimax com Poda Alfa-Beta{RESET}")
            return "alphabeta"
        else:
            print(f"\n  {RED}⚠{RESET} Opção inválida, tente novamente.")
            input(f"\n  {DIM}Pressione ENTER para continuar...{RESET}")   

def exibirResultados(algoritmo: str, historicoJogadas: list, historicoValores: list, historicoNos: list, historicoTempos: list):
    """Exibe todos os resultados em uma única seção."""
    limpar()
    print(f"""
{BOLD}{CYAN}
┌─────────────────────────────────────────────────┐
│                                                 │
│              ✦  RESULTADOS  ✦                   │
│                                                 │
{RESET}  Algoritmo: {BOLD}{WHITE}{algoritmo}{RESET}
{BOLD}{CYAN}│  ─────────────────────────────────────────────  │
│                                                 │
""")

    for i in range(len(historicoJogadas)):
        jogada = historicoJogadas[i]
        valor = historicoValores[i]
        nos = historicoNos[i]
        tempo = historicoTempos[i]
        print(f"""{BOLD}{CYAN}  ┌─────────────────────────────────────────────┐
  │ {RESET}{BOLD}{YELLOW}Jogada {i+1}{RESET}{BOLD}{CYAN}{'│'}
  │ {RESET}Posição: {BOLD}{WHITE}{jogada}{RESET}    Valor: {BOLD}{GREEN}{valor}{RESET}
  │ {RESET}Nós: {BOLD}{WHITE}{nos}{RESET}              Tempo: {BOLD}{MAGENTA}{tempo:.4f} ms{RESET}
{BOLD}{CYAN}  └─────────────────────────────────────────────┘{RESET}
""")

    print(f"""{BOLD}{CYAN}│  ─────────────────────────────────────────────  │
│                                                 │
{RESET}{DIM}└─────────────────────────────────────────────────┘{RESET}
""")
    input(f"\n  {DIM}Pressione ENTER para continuar...{RESET}")   