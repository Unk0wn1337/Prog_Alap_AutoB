#név$gyártási dátum
class Auto:
    def __init__(self,sor:str):
        adatok = sor.strip().split("$")
        self.nev = adatok[0]
        self.datum = int(adatok[1])
    def __str__(self):
        return f"nev: {self.nev} gyartasi datum: {self.datum}"