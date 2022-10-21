class Fejlesztő:
    def __init__(self, nev, fizetes, rang="Junior", dolgozottEv=0) -> None:
        self.nev = nev
        self.fizetes = fizetes
        self.rang = rang
        self.dolgozottEv = dolgozottEv

    def fizEmel(self, osszeg=10000):
        self.fizetes += osszeg
        print(self.fizetes)

    def hozzadEvet(self):
        self.dolgozottEv += 1
        print(self.dolgozottEv)
    def rangotMegallapit(self):
        if  2 >= self.dolgozottEv >= 1 :
            self.rang = "Junior"
        elif 5 >= self.dolgozottEv > 2:
            self.rang = "Medior"
        elif self.dolgozottEv > 5:
            self.rang = "Senior"
        else:
            self.rang = "Intern"
        print(self.rang)
        

def main():
    Peti = Fejlesztő("Péter", 8000000,"Senior", 0)
    Peti.fizEmel(12000)
    Peti.hozzadEvet()
    Peti.rangotMegallapit()


main()
