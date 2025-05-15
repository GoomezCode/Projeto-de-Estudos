# 1. Calculadora Simples
# 2. jogo de adivinhação com While
# 3. Cadastro de usuários com Input() + listas
# 4. Mini agenda com arquivos .txt
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def desafio01():
    operacao = input("Qual a operação da conta? | X | + | - | / | : ").lower()
    num1 = int(input("Primeiro Num? : "))
    num2 = int(input("Segundo Num? : "))

    if operacao == "x":
        resultado = num1 * num2
    elif operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        print("ERROR-404")

    print(f"O resultado da conta é {resultado}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random

def desafio02():
    numAleatorio = random.randint(1, 10)
    tentativas = 0
    while True:
        repostaPessoa = int(input("Fala um numero de (1 a 10) : "))
        tentativas += 1

        if repostaPessoa == numAleatorio:
            print("Acertou o numero")
            print(f"Você teve {tentativas} para acertar")
            break
        elif repostaPessoa < numAleatorio:
            print(f"O numero {repostaPessoa} e menor que o numero aleatorio")
            print()
        elif repostaPessoa > numAleatorio:
            print(f"O numero {repostaPessoa} e maior que o numero aleatorio")
            print()


