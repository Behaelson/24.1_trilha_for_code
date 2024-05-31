import secrets

alimentos = ["banana", "batata", "cebola", "arroz", "limão", "feijão", "frango", "ratatouille", "almondega", "atum", "salmão", "sushi"]

# print("Bem vindo ao Jogo da Forca genéricoTM!", '\n', "O Tema é: Alimentos.")
# inicio = str.lower(input("Você deseja adicionar um alimento extra a lista? "))
# if inicio == "sim":
#    alimentos.append(str.lower(input("Insira o alimento que deseja estar na lista:")))

forca = secrets.choice(alimentos)
falha = 0
letrasU = []
palavrasU = []
forca_progresso = len(forca)*"-"

while falha < 5:
    print(forca_progresso)
    tentativa = input("Escolha uma letra, você tem direito a 5 falhas: ").lower()
    if len(tentativa) == 1 and tentativa.isalpha:
        if tentativa not in forca:
            print(tentativa, "Não pertence a palavra, tente novamente.")
            letrasU.append(tentativa)
            falha += 1
        elif tentativa in letrasU:
            print("Essa letra já foi usada, tente outra! Letras que já foram escolhidas: ", letrasU)
        else:
            letrasU.append(tentativa)
            if tentativa in list(forca)
            if "-" not in palavra:
                guessed = True
            

    elif len(tentativa) == len(forca):
    
    else:
        print("Não corresponde ao alfabeto, tente novamente:")



    

