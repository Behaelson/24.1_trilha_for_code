import random
import time

a = "Pedra"
b = "Papel"
c = "Tesoura"

# a > b > c and c > a

Escolhas = (a, b, c)
tentativas = 0
vitorias = 0

PC = random.choice(Escolhas)

while tentativas < 5:
    if vitorias == 3:
        print("LEsgoooo")
        break
    print("Pedra, Papel ou Tesoura?"), '\n'
    P1 = input()  
    if P1 in Escolhas: 
        # print("Jô")
        # time.sleep(0.5)
        # print("Ken")
        # time.sleep(0.5)
        # print("Pô!")
        # time.sleep(1.0) 
        print(PC)
        # PCind = Escolhas.index(PC)
        # P1ind = Escolhas.index(P1)
        tentativas = tentativas + 1
        if P1 > PC:
           print("Perdeu!") 
        elif P1 == PC:
            print("Empate")
        else:
            print("Ganhou!")
            vitorias = vitorias + 1
        

print("CABO")