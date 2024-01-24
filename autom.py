import Auto

f = open("auto.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def harmadikElso():
    index = 0
    leghosszabb = 0
    leghosszabbNeve = ""
    while index < len(sorok):
        Autok = Auto.Auto(sorok[index])
        if Autok.datum > leghosszabb:
            leghosszabb = Autok.datum
            leghosszabbNeve = Autok.nev
        index+=1
    print(f"III/Tabla:\n\t{leghosszabbNeve}: 11 hosszú")


def harmadikMasodik():
    index = 0
    while index < len(sorok):
        index+=1
    print(f"III/Flotta:\n\tAutok szama: {index}")

def harmadikHarmadik():
    index = 0
    legfiatalabbAuto = 2000
    legfiatalabbAutoNeve = ""
    while index < len(sorok):
        Autok = Auto.Auto(sorok[index])
        if Autok.datum > legfiatalabbAuto:
            legfiatalabbAutoNeve = Autok.nev
            legfiatalabbAuto = Autok.datum
        index+=1
    print(f"III/Értékes\n\tA legfiatalabb autó: {legfiatalabbAutoNeve}({legfiatalabbAuto}))")






