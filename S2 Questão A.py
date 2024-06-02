import secrets

alimentos = ["banana", "batata", "cebola", "arroz", "limao", "feijao", "frango", "ratatouille", "almondega", "atum", "salmao", "sushi"]
forca = (secrets.choice(alimentos))

print("Bem vindo ao Jogo da Forca genéricoTM!", '\n', "O Tema é: Alimentos.")
inicio = str.lower(input("Você deseja adicionar um alimento extra a lista? "))
if inicio == "sim":
   alimentos.append(str.lower(input("Insira o alimento que deseja estar na lista:")))

falha = 0
letrasU = []
palavrasU = []
forca_escondida = len(forca)*"-"
acerto = False

while falha < 6 or acerto == True:
    print(forca_escondida)
    tentativa = input("Escolha uma letra, você tem direito a 6 falhas: ").lower()
    if len(tentativa) == 1 and tentativa.isalpha:
        if tentativa not in forca:
            print(tentativa, "Não pertence a palavra, tente novamente.")
            letrasU.append(tentativa)
            falha += 1
        elif tentativa in letrasU:
            print("Essa letra já foi usada, tente outra! Letras que já foram escolhidas: ", letrasU)
        else:
            forca_list = list(forca_escondida)
            letrasU.append(tentativa)
            troca_de_hifen = [i for i, X in enumerate(forca) if X == tentativa]
            for B in troca_de_hifen:
                forca_list[B] = tentativa
                forca_escondida = "".join(forca_list)

            if "-" not in forca_escondida:
                acerto = True
                print("Parabéns! É isso mesmo!")
                break
            
    elif len(tentativa) == len(forca) and tentativa.isalpha:
        if tentativa != forca:
            print(tentativa, "não é a palavra.")
            falha += 1
            palavrasU.append(tentativa)
        elif tentativa in palavrasU:
                print("Você já tentou essa palavra, tente outra.")
        else:
            acerto = True
            forca_escondida = forca
            print("Parabéns! É isso mesmo!")
            break
        
    else:
        print("Não corresponde ao alfabeto, tente novamente:")

if acerto == False:
        print("Poxa, não foi dessa vez, a palavra era: " + forca)
