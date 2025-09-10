# 🧙‍♂️ RPG de Terminal

Um jogo simples em Python rodando no terminal, onde você controla um personagem (`@`) que deve atravessar um labirinto (`X`) até chegar ao objetivo (`C`). Feito como exercício de lógica, leitura de arquivos e interação com o usuário.

---

## 📁 Estrutura do Projeto

```
rpg-terminal/
├── mapa.txt
└── rpg_terminal.py
```

---

## 🎮 Como Jogar

1. Clone o repositório:

   ```bash
   git clone https://github.com/gontin/terminal-rpg.git
   cd rpg-terminal
   ```

2. Crie (ou edite) o arquivo `mapa.txt` com seu mapa personalizado:

   ```txt
   XXXXXXXXXX
   X@.......X
   X..X.X...X
   X....X..CX
   XXXXXXXXXX
   ```

3. Execute o jogo:

   ```bash
   python rpg_terminal.py
   ```

4. Comandos disponíveis:

   ```
   W - mover para cima
   A - mover para esquerda
   S - mover para baixo
   D - mover para direita
   X - sair do jogo
   ```

---

## 📜 Tecnologias Utilizadas

* Python 3
* Terminal / Console
* Manipulação de arquivos (`.txt`)
* Estruturas de controle e listas aninhadas

---

## 🧠 Aprendizados

* Leitura e processamento de arquivos externos
* Controle de fluxo com loops e funções
* Tratamento de erros com `try/except`
* Representação visual de dados no terminal

---

## 🛠️ Melhorias Futuras

* Novos níveis com múltiplos mapas
* Sistema de vidas ou pontuação
* Visuais mais detalhados (com emojis ou `curses`)
* Exportar pontuação ou progresso

---

## 👤 Autor

**Gustavo Silveira Nicoletti**
Desenvolvedor Full Stack
[GitHub - gontin](https://github.com/gontin)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo.
