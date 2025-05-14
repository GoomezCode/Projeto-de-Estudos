
def compraPão():
    # 1. Crie um programa onde o preço do pão será guardado em uma variável. Aós isso, o usuário digitará quanto ele tem. Caso ele tenha donheiro sificient, uma Mensagem será exibida informando que ele comprou o pão, Caso contrário, Inventa um nome ai

    money = float(input("Você tem quantos no carteira? : "))

    quantidadePao = int(input("Quantos Pães você quer pegar? : "))
    custoPao = 0.75
    somaPreço = quantidadePao * custoPao

    if money >= somaPreço:
        print("Compra finalizada com sucesso!")
    else:
        print("Não tem o Dinheiro para a compra!!")


def temperatura():
    # 2. Crie uma variável "temperatura" e exiba uma mensagem diferente para cada situação. "Frio" para quando estiver baixa, "Normal" quando estiver normal, e "quente" quando estiver alto

    temperatura = input("Qual a temperatura de sua cidade? : ")

    if temperatura <= "15":
        temperatura += "°C"
        print(f"A temperatura {temperatura} está baixa o clima está Frio")
    elif temperatura <= "20"  <= "28" :
        temperatura += "°C"
        print(f"A Temperatura {temperatura} está estavel o clima está Normal")
    elif temperatura >= "30":
        temperatura += "°C"
        print(f"A temperatura {temperatura} está Elevada o clima está Quente") 




def Atleta():
    # 3. Crie um programa para avaliar a entrada de atletas em uma competição olímpica. Para entrar, o atleta deverá ter entre 18 e 35 anos. Ele também prescisa ter um bom condicionamento físico ou permisão médica. As condições devem ser feitas em uma úncia estrutura if

    nomeAtleta = input("Qual o seu nome? : ").lower()
    idadeAtleta = int(input("Quantos anos vc tem? "))
    fisicoAtleta = True
    permissaoMedica = True

    if idadeAtleta >=18 <=36 and fisicoAtleta == True or permissaoMedica == True:
        print(f"{nomeAtleta} Você vai poder Competir nas olímpiadas")
    else:
        print(f"{nomeAtleta} Vocẽ não tem o resquisitos para isso")

