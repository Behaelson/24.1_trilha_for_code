import secrets

alimentos = ["banana", "batata", "cebola", "arroz", "limao", "feijao", "frango", "ratatouille", "almondega", "atum", "salmao", "sushi"]

# print("Bem vindo ao Jogo da Forca genéricoTM!", '\n', "O Tema é: Alimentos.")
# inicio = str.lower(input("Você deseja adicionar um alimento extra a lista? "))
# if inicio == "sim":
#    alimentos.append(str.lower(input("Insira o alimento que deseja estar na lista:")))

forca = (secrets.choice(alimentos))
falha = 0
letrasU = []
palavrasU = []
forca_escondida = len(forca)*"-"

while falha < 5:
    print(forca_escondida)
    tentativa = input("Escolha uma letra, você tem direito a 5 falhas: ").lower()
    if len(tentativa) == 1 and tentativa.isalpha:
        if tentativa not in forca:
            print(tentativa, "Não pertence a palavra, tente novamente.")
            letrasU.append(tentativa)
            falha += 1
        elif tentativa in letrasU:
            print("Essa letra já foi usada, tente outra! Letras que já foram escolhidas: ", letrasU)
        else:
            forca_list = list(forca)
            troca_de_hifen = [i for i, X in enumerate(forca_list) if X == tentativa]
            for B in troca_de_hifen:
                forca_list[B] = tentativa
                forca_escondida = "".join(forca_list)

            if "-" not in forca_escondida:
                print("Parabéns!!!")
                break
            
                
            

    # elif len(tentativa) == len(forca):
    
    # else:
    #     print("Não corresponde ao alfabeto, tente novamente:")



    

