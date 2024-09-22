with open('mapa.txt', 'r') as mapa:
    mapa = mapa.read()
listadaslinhas = mapa.splitlines()
mapa = list(map(list, listadaslinhas))

ganhou = False

def acharplayer(mapita):         # i = linha   a = coluna
    for i in range(len(mapita)):
        for a in range(len(mapita[i])):
            if mapita[i][a] == '@':
                return [i,a]

def movarcima(iplayer, aplayer):
    global ganhou
    try:
        if mapa[iplayer-1][aplayer] == 'X':
            print("impossivel a passagem")
        elif mapa[iplayer-1][aplayer] == 'C':
            ganhou = True
        elif mapa[iplayer-1][aplayer] == '.':
            mapa[iplayer][aplayer] = '.'
            mapa[iplayer-1][aplayer] = '@'
    except IndexError:
        print("ta tentando ir pra narnia oh arrombado")


def movarbaixo(iplayer, aplayer):
    global ganhou
    try:
        if mapa[iplayer+1][aplayer] == 'X':
            print("impossivel a passagem")
        elif mapa[iplayer+1][aplayer] == 'C':
            ganhou = True
        elif mapa[iplayer+1][aplayer] == '.':
            mapa[iplayer][aplayer] = '.'
            mapa[iplayer+1][aplayer] = '@'
    except IndexError:
        print("ta tentando ir pra narnia oh arrombado")


def movardireita(iplayer, aplayer):
    global ganhou
    try:
        if mapa[iplayer][aplayer+2] == 'X':
            print("impossivel a passagem")
        elif mapa[iplayer][aplayer+2] == 'C':
            ganhou = True
        elif mapa[iplayer][aplayer+2] == '.':
            mapa[iplayer][aplayer] = '.'
            mapa[iplayer][aplayer+2] = '@'
    except IndexError:
        print("ta tentando ir pra narnia oh arrombado")

def movaresquerda(iplayer, aplayer):
    global ganhou
    try:
        if mapa[iplayer][aplayer-2] == 'X':
            print("impossivel a passagem")
        elif mapa[iplayer][aplayer-2] == 'C':
            ganhou = True
        elif mapa[iplayer][aplayer-2] == '.':
            mapa[iplayer][aplayer] = '.'
            mapa[iplayer][aplayer-2] = '@'
    except IndexError:
        print("ta tentando ir pra narnia oh arrombado")
        

while True:
    if ganhou == True:
        print("YAAAAAAAAAAAYYYY VC GANHOU *CLAP CLAP CLAP*\n░░░░█░▀▄░░░░░░░░░░▄▄███▀░░\n░░░░█░░░▀▄░▄▄▄▄▄░▄▀░░░█▀░░\n░░░░░▀▄░░░▀░░░░░▀░░░▄▀░░░░\n░░░░░░░▌░▄▄░░░▄▄░▐▀▀░░░░░░\n░░░░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█\n░░░░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█\n░░░▄▀▀▐▀▀░░░░░░░▀▀▌▄▄▄░░░█\n░░░█░░░▀▄░░░░░░░▄▀░░░░█▀▀▀\n░░░░▀▄░░▀░░▀▀▀░░▀░░░▄█░░░░")
       
        break
    print('~~~~~~~~~~~~~~~~~~~~~~~~~RPG-DE-TERMINAL~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                    W - MOVER PARA CIMA')
    print('                    A - MOVER PARA ESQUERDA')
    print('                    S - MOVER PARA BAIXO')
    print('                    D - MOVER PARA DIREITA')
    print('                    X - SAIR')
    print('                    OBJETIVO = CHEGAR NO C')
    
    

    playerloc = acharplayer(mapa)
    for i in mapa:
        for a in i:
            print(f"{a}", end='')
        print()
    
    esc = input('sua escolha: ').strip().lower()


    if esc == 'w':
        movarcima(playerloc[0], playerloc[1])
    elif esc == 'a':
        movaresquerda(playerloc[0], playerloc[1])
    elif esc == 's':
        movarbaixo(playerloc[0], playerloc[1])
    elif esc == 'd':
        movardireita(playerloc[0], playerloc[1])
    elif esc == 'x':
        print("Obrigado por jogar <3")
        break