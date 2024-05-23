import secrets

alimentos = ["banana", "batata", "cebola", "arroz", "limão", "feijão", "frango", "ratatouille", "almondega", "atum", "salmão", "sushi"]

print("Bem vindo ao Jogo da Forca genéricoTM! O Tema é: Alimentos.")
inicio = str.lower(input("Você deseja adicionar um alimento extra a lista? "))
alimentos.append(str.lower(input("Insira o alimento que deseja estar na lista:")))

print(alimentos)