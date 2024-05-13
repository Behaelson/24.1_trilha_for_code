import random
import time 

Escolhas = ("pedra", "papel", "tesoura")
tentativas = 0
vitorias = 0
derrotas = 0

PC = random.choice(Escolhas)

while tentativas < 5:
    if vitorias >= 3:
        print("Parabéns! Você ganhou!! :D")
        break
    if derrotas >= 3:
        print("Que pena! Você perdeu! :(")
        break
    print('\n', "Pedra, Papel ou Tesoura?"), '\n'
    P1 = str.lower(input("Escolha do Jogador: "))
    if P1 in Escolhas: 
        print("Jô")
        time.sleep(0.5)
        print("Ken")
        time.sleep(0.5)
        print("Pô!")
        time.sleep(1.0) 
        print("Escolha do adversário:", PC)
        PCind = Escolhas.index(PC)
        P1ind = Escolhas.index(P1)
        PX = P1ind - PCind
        tentativas = tentativas + 1
        if PX == 1 or PX == -2:
           print("Ganhou!") 
           vitorias = vitorias + 1
        elif PX == 0:
            print("Empate!")
        else:
            print("Perdeu!")
            derrotas = derrotas + 1

final = vitorias - derrotas
if final > 0:
    print("Parabéns, você ganhou por pouco!")
elif final == 0:
    print("É... Empatou de vez!")
else:
    print("Mesmo sem perder 3 vezes... você perdeu no final... ;-;")