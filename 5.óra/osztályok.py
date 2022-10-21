class BankSzamla:
    def __init__(self,nev,egyenleg,) -> None:
        self.__class__dupont = 1000 # self az olyan mint a this.
        self.nev = nev
        self.egyenleg = egyenleg
    def betesz(self,osszeg):
        self.egyenleg += osszeg
    def kivesz(self,osszeg):
        if osszeg > self.egyenleg:
            print("Nincs megfelelő money!")
        else:
            self.egyenleg -= osszeg
            print("Egyenleg: {0}".format(self.egyenleg))
    def kiir(self):
        print("Tulaj: {1}, Összeg: {2}".format(self.nev, self.egyenleg))
        
        
def main():
    b1 = BankSzamla("Béla", 600)
    
    b1.kivesz(200)
if __name__ == "__main__":
    main()