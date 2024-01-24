import random
lista = []
index = 0
while index < 50:
    randomSzam = random.randint(1,100)
    lista.append(randomSzam)
    index+=1

def kiiratas():
    index = 0
    while index < len(lista):
        if index == 0:
            print(f"{lista[index]}$",end="")
        else:
            print(f"${lista[index]}",end="")
        index+=1
    print(f"\nHettel oszhatóak: {hettelOszhatoak()} Öttel oszthatóak: {ottelOszhato()}")


def ottelOszhato():
    index = 0
    szam = 0
    while index < len(lista):
        if lista[index] % 5 == 0:
            szam+=1
        index+=1
    return szam


def hettelOszhatoak():
    index = 0
    szam = 0
    while index < len(lista):
        if lista[index] % 7 == 0:
            szam += 1
        index += 1
    return szam
