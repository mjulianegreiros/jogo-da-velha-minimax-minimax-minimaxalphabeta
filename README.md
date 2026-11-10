# 🎀 Jogo da Velha — Minimax & Alfa-Beta

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/IA-Busca%20Competitiva-ff69b4" />
  <img src="https://img.shields.io/badge/Algoritmos-Minimax%20%7C%20Alfa--Beta-purple" />
</p>

<p align="center">
  <i>Um clássico jogo da velha com um toque de Inteligência Artificial! ♡</i>
</p>

---

## 🌷 Sobre o projeto

Este projeto consiste no desenvolvimento de uma versão interativa do **Jogo da Velha**, na qual uma pessoa pode jogar contra um computador que utiliza algoritmos de busca competitiva para tomar suas decisões.

O objetivo principal é estudar e implementar os algoritmos **Minimax** e **Minimax com Poda Alfa-Beta**, compreendendo como eles exploram possibilidades futuras para escolher jogadas estrategicamente melhores.

O projeto foi desenvolvido como atividade prática da disciplina de **Inteligência Artificial**, da Universidade Federal do Ceará (UFC) — Campus Crateús.

## ✨ Funcionalidades

- 🎮 Partidas entre uma pessoa e o computador.
- ❎ Escolha do símbolo: X ou O.
- 🧠 Seleção entre Minimax e Minimax com Poda Alfa-Beta.
- ♟️ Exibição do tabuleiro e das jogadas disponíveis.
- 🚫 Validação de jogadas para impedir posições inválidas ou ocupadas.
- 🏆 Identificação de vitória, derrota e empate.
- 📊 Exibição de métricas das decisões do computador:
  - Posição escolhida;
  - Valor Minimax;
  - Quantidade de nós visitados;
  - Tempo de execução.

## 🧠 Algoritmos implementados

### 1. Minimax

O Minimax é um algoritmo de busca utilizado em jogos de dois jogadores, considerando que ambos tomam decisões de maneira ótima.

Neste projeto:

- **X:** representa o jogador MAX, que busca maximizar a pontuação.
- **O:** representa o jogador MIN, que busca minimizar a pontuação.

A avaliação dos estados finais utiliza os seguintes valores:

| Resultado | Pontuação |
|:---:|:---:|
| Vitória de X | +1 |
| Empate | 0 |
| Vitória de O | -1 |

### 2. Minimax com Poda Alfa-Beta

A poda Alfa-Beta é uma otimização do Minimax que evita explorar determinados ramos da árvore de busca quando eles não podem influenciar a decisão final.

São utilizados dois limites:

- **Alfa (α):** melhor valor encontrado até então para MAX.
- **Beta (β):** melhor valor encontrado até então para MIN.

A poda ocorre quando α ≥ β, reduzindo a quantidade de nós explorados sem alterar o valor minimax da decisão.

## 📁 Estrutura do projeto

```text
tic-tac-toe/
│
├── agente.py       # Controle das decisões do computador
├── interface.py    # Interação com o usuário
├── main.py         # Execução e organização da partida
├── minimax.py      # Implementação dos algoritmos de busca
├── regras.py       # Regras e condições de encerramento
└── tabuleiro.py    # Criação e manipulação do tabuleiro
```

## 🚀 Como executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou editor de código de sua preferência.

### Executando o projeto

1. Clone o repositório:

```bash
git clone [URL_DO_REPOSITORIO](https://github.com/mjulianegreiros/jogo-da-velha-minimax-minimax-minimaxalphabeta/)
```

2. Entre na pasta do projeto:

```bash
cd tic-tac-toe
```

3. Execute o arquivo principal:

```bash
python main.py
```

> Caso seu sistema utilize o comando `python3`, execute `python3 main.py`.

## 📊 Métricas e experimentação

Além de permitir partidas interativas, o projeto registra informações sobre o desempenho dos algoritmos.

As métricas coletadas permitem observar:

- Quantidade de nós visitados durante a busca;
- Tempo necessário para escolher uma jogada;
- Valor minimax associado à decisão;
- Diferenças de desempenho entre Minimax e Alfa-Beta.

Essas informações servem como base para analisar o impacto da poda Alfa-Beta na exploração da árvore de possibilidades.

## 🎓 Informações acadêmicas

| Informação | Descrição |
|---|---|
| Instituição | Universidade Federal do Ceará — UFC |
| Disciplina | Inteligência Artificial |
| Trabalho | Busca Competitiva — Minimax e Poda Alfa-Beta no Jogo da Velha |

---

<p align="center">
  ♡ <b>Desenvolvido para fins acadêmicos e de aprendizado.</b> ♡
  <br/>
  <i>Explorando possibilidades, uma jogada por vez! 🎀</i>
</p>
