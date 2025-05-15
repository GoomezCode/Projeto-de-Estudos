# Sistema Random
import random

# Número aleatório inteiro entre dois valores
def a():
    a = random.randint(1,10)
    print(a)

#Número decimal aleatório entre 0 e 1
def b():
    b = random.random()
    print(b)

# Número decimal entre dois valores (float)
def c():
    c = random.uniform(1.0, 10.0)
    print(c)

# Escolher item aleatório de uma lista
def d(frutas):
    frutas = ["maça", "banana", "Uva", "laranja", "Melancia"]
    c = random.choice(frutas)
    print(c)
# Embaralhar uma lista
def e(num):
    num = ["A", "B", "C"]
    e = random.shuffle(num)
    print(e)

def f(alunos):
    alunos = ['Ana', 'Bruno', 'Carlos', 'Duda']
    sorteados = random.sample(alunos, 2)
    print(sorteados)
    return sorteados


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
